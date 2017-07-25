from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, FormField, SubmitField
from wtforms.validators import DataRequired

from aeon_ztp.ztp_os_selector import fact_match_list


class OsSelectorMatch(FlaskForm):
    fact_match_type = SelectField('Match Type', choices=fact_match_list())
    fact_match_string = StringField('Fact Match Text', validators=[DataRequired()])


class OsSelectorForm(FlaskForm):
    group = StringField('Group Name', validators=[DataRequired()])
    vendor = SelectField('Vendor', choices=[('eos', 'EOS'), ('nxos', 'NXOS'), ('cumulus', 'Cumulus')])
    os_match_type = SelectField('Match Type', choices=[('exact_match', 'Exact'), ('regex_match', 'Regex')])
    version_match = StringField('Version Match', validators=[DataRequired()])
    finally_script = StringField('Finally Script', validators=[DataRequired()])
    image = StringField('Image Name', validators=[DataRequired()])
    fact_match = FormField(OsSelectorMatch)
    submit = SubmitField('Create')


class OsSelectorDelete(FlaskForm):
    group = StringField('Group Name', validators=[DataRequired()])
    vendor = StringField('Vendor', validators=[DataRequired()])
    submit = SubmitField('Delete')
