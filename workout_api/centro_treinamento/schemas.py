from typing import Annotated

from pydantic import Field
from workout_api.contrib.schemas import BaseSchema


class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description = 'Nome do Centro de treinamento', example = 'CT King', max_length = 20)]
    endereço: Annotated[str, Field(description = 'Endereço do Centro de treinamento', example = 'Rua x quadra 002', max_length = 60)]
    nome: Annotated[str, Field(description = 'Proprietario do Centro de treinamento', example = 'Marcos', max_length = 30)]