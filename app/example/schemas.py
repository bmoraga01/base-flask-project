from marshmallow import fields
from ..ext import marshmallow
from .models import Band, Member

class MemberSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Member
        
    id              = marshmallow.auto_field()
    name            = marshmallow.auto_field()
    nickname        = marshmallow.auto_field()
    birthdate       = marshmallow.auto_field()
    instruments     = marshmallow.auto_field()
    id_band         = marshmallow.auto_field()

class BandSchema(marshmallow.SQLAlchemySchema):
    class Meta:
        model = Band
    
    id          = marshmallow.auto_field()
    name        = marshmallow.auto_field()
    origin      = marshmallow.auto_field()
    state       = marshmallow.auto_field()
    gender      = marshmallow.auto_field()
    founded     = marshmallow.auto_field()
    members     = fields.Nested(MemberSchema(), many=True)