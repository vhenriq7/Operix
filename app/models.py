from sqlalchemy import ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Organizacao(Base):
    __tablename__ = "organizacoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome: Mapped[str]
    filiais: Mapped[list["Filial"]] = relationship(back_populates="organizacao")


class Filial(Base):
    __tablename__ = "filiais"

    id: Mapped[int] = mapped_column(primary_key=True)
    organizacao_id: Mapped[int] = mapped_column(ForeignKey("organizacoes.id"))
    nome: Mapped[str]
    organizacao: Mapped["Organizacao"] = relationship(back_populates="filiais")
