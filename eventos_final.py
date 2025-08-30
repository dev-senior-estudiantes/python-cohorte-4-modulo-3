from dataclasses import dataclass
from typing import Dict, List, Iterable, Generator
from collections import Counter, defaultdict
import unicodedata

def nfkc(s: str) -> str:
    return unicodedata.normalize("NFKC", s)

def norm_text(s) -> str:
    if s is None:
        return ""
    s = " ".join(nfkc(str(s)).strip().split())
    return s.casefold()

def no_acentos(s: str) -> str:
    nk = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in nk if unicodedata.category(ch) != "Mn")

is_nonempty = lambda s: bool(s and s.strip())

def pipeline_personas(rows: Iterable[dict]) -> Generator[dict, None, None]:
    gen = (
        {"email": no_acentos(norm_text(r.get("email", ""))),
         "nombre": no_acentos(norm_text(r.get("nombre", "")))}
        for r in rows
    )
    gen = (r for r in gen if is_nonempty(r["email"]) and "@" in r["email"])
    return gen

@dataclass(frozen=True)
class Venue:
    id: int
    ciudad: str
    nombre: str
    capacidad: int

@dataclass(frozen=True)
class Event:
    id: int
    nombre: str
    fecha: str
    venue_id: int

@dataclass(frozen=True)
class Attendee:
    id: int
    email: str
    nombre: str

@dataclass
class Registration:
    event_id: int
    attendee_id: int

class EventManager:
    def __init__(self):
        self.venues: Dict[int, Venue] = {}
        self.events: Dict[int, Event] = {}
        self.attendees: Dict[int, Attendee] = {}
        self.regs: List[Registration] = []
        self.idx_eventos_por_fecha: Dict[str, List[int]] = defaultdict(list)
        self.idx_attendee_por_email: Dict[str, int] = {}
        self._next_vid = 1
        self._next_eid = 1
        self._next_aid = 1

    def add_venue(self, ciudad: str, nombre: str, capacidad: int) -> int:
        v = Venue(self._next_vid, norm_text(ciudad), norm_text(nombre), int(capacidad))
        self.venues[v.id] = v
        self._next_vid += 1
        return v.id

    def add_event(self, nombre: str, fecha: str, venue_id: int) -> int:
        e = Event(self._next_eid, norm_text(nombre), norm_text(fecha), venue_id)
        self.events[e.id] = e
        self.idx_eventos_por_fecha[e.fecha].append(e.id)
        self._next_eid += 1
        return e.id

    def upsert_attendee(self, email: str, nombre: str) -> int:
        email_n = no_acentos(norm_text(email))
        if "@" not in email_n:
            raise ValueError("Email inválido")
        if email_n in self.idx_attendee_por_email:
            aid = self.idx_attendee_por_email[email_n]
            if is_nonempty(nombre):
                a = self.attendees[aid]
                self.attendees[aid] = Attendee(a.id, email_n, no_acentos(norm_text(nombre)))
            return aid
        aid = self._next_aid
        self.attendees[aid] = Attendee(aid, email_n, no_acentos(norm_text(nombre)))
        self.idx_attendee_por_email[email_n] = aid
        self._next_aid += 1
        return aid

    def register(self, event_id: int, attendee_id: int) -> None:
        if any(r.event_id == event_id and r.attendee_id == attendee_id for r in self.regs):
            return
        e = self.events[event_id]
        v = self.venues[e.venue_id]
        ocupados = sum(1 for r in self.regs if r.event_id == event_id)
        if ocupados >= v.capacidad:
            raise RuntimeError("Capacidad completa")
        self.regs.append(Registration(event_id, attendee_id))

    def eventos_por_fecha(self, fecha: str) -> List[Event]:
        return [self.events[i] for i in self.idx_eventos_por_fecha.get(norm_text(fecha), [])]

    def asistentes_de_evento(self, event_id: int) -> List[Attendee]:
        aids = [r.attendee_id for r in self.regs if r.event_id == event_id]
        return [self.attendees[i] for i in aids]

    def eventos_por_ciudad(self, ciudad: str) -> List[Event]:
        c = norm_text(ciudad)
        vids = [v.id for v in self.venues.values() if v.ciudad == c]
        return [e for e in self.events.values() if e.venue_id in vids]

    def duplicados_por_email(self) -> set:
        emails = [a.email for a in self.attendees.values()]
        vistos, dups = set(), set()
        for em in emails:
            if em in vistos:
                dups.add(em)
            else:
                vistos.add(em)
        return dups

    def top_ciudades_por_eventos(self, k=3):
        from collections import Counter
        ciudades = [self.venues[e.venue_id].ciudad for e in self.events.values()]
        return Counter(ciudades).most_common(k)

    def ocupacion_por_evento(self) -> Dict[int, float]:
        def ocup(e: Event) -> float:
            v = self.venues[e.venue_id]
            inscritos = sum(1 for r in self.regs if r.event_id == e.id)
            return round(100.0 * inscritos / max(1, v.capacidad), 2)
        return {e.id: ocup(e) for e in self.events.values()}

if __name__ == "__main__":
    em = EventManager()
    v1 = em.add_venue("Bogotá", "Centro Convenciones", 3)
    v2 = em.add_venue("Medellín", "Plaza Mayor", 2)
    e1 = em.add_event("Conferencia Python", "2025-09-20", v1)
    e2 = em.add_event("Taller IA", "2025-09-25", v2)

    sucios = [
        {"email": "  ANA@mail.com ", "nombre": "Ana"},
        {"email": "luis@mail.COM", "nombre": "Luis"},
        {"email": "maria@mail.com", "nombre": "María"},
        {"email": "maria@mail.com", "nombre": "Maria"},
        {"email": "invalido", "nombre": "X"},
    ]

    for fila in pipeline_personas(sucios):
        aid = em.upsert_attendee(fila["email"], fila["nombre"])
        em.register(e1, aid)

    try:
        extra = em.upsert_attendee("extra@mail.com", "Extra")
        em.register(e1, extra)
    except RuntimeError as err:
        print("[WARN]", err)

    print("Eventos 2025-09-20:", em.eventos_por_fecha("2025-09-20"))
    print("Asistentes de e1:", em.asistentes_de_evento(e1))
    print("Eventos en Medellín:", em.eventos_por_ciudad("MEDELLÍN"))
    print("Duplicados por email:", em.duplicados_por_email())
    print("Top ciudades por eventos:", em.top_ciudades_por_eventos())
    print("Ocupación por evento (%):", em.ocupacion_por_evento())

