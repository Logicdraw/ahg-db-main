from main.crud._base.spng_survey import spng_survey_base_crud


from main.crud._many.camp_instances_coaches import camp_instances_coaches_crud
from main.crud._many.program_instances_coaches import program_instances_coaches_crud
from main.crud._many.team_instances_coaches import team_instances_coaches_crud
from main.crud._many.team_instances_players import team_instances_players_crud
from main.crud._many.spng_surveys_spng_survey_questions import spng_surveys_spng_survey_questions_crud
from main.crud._many.guardians_players import guardians_players_crud


from main.crud.data.person.coach import coach_crud
from main.crud.data.person.guardian import guardian_crud
from main.crud.data.person.player import player_crud

from main.crud.data.camp import camp_crud
from main.crud.data.camp.group import camp_group_crud
from main.crud.data.camp.group.instance import camp_group_instance_crud
from main.crud.data.camp.instance import camp_instance_crud
from main.crud.data.camp.instance.registration import camp_instance_registration_crud

from main.crud.data.program import program_crud
from main.crud.data.program.group import program_group_crud
from main.crud.data.program.group.instance import program_group_instance_crud
from main.crud.data.program.instance import program_instance_crud
from main.crud.data.program.instance.registration import program_instance_registration_crud

from main.crud.data.team import team_crud
from main.crud.data.team.conference import conference_crud
from main.crud.data.team.division import division_crud
from main.crud.data.team.league import league_crud
from main.crud.data.team.season import season_crud

from main.crud.data.team.instance import team_instance_crud
from main.crud.data.team.instance.conference import conference_instance_crud
from main.crud.data.team.instance.division import division_instance_crud
from main.crud.data.team.instance.league import league_instance_crud
from main.crud.data.team.instance.season import season_instance_crud

from main.crud.data.team.instance.orders.jersey_socks import team_instance_jersey_socks_order_crud
from main.crud.data.team.instance.orders.tracksuit import team_instance_tracksuit_order_crud

from main.crud.data.team.instance.registration import team_instance_registration_crud
from main.crud.data.team.instance.registration.jersey_sponsor import team_instance_registration_jersey_sponsor_crud

from main.crud.external.spng_survey.camp import spng_survey_camp_crud
from main.crud.external.spng_survey.program import spng_survey_program_crud
from main.crud.external.spng_survey.team import spng_survey_team_crud

from main.crud.external.spng_survey_question import spng_survey_question_crud
from main.crud.external.spng_survey_question.table_map import spng_survey_question_table_map_crud

from main.crud.form import form_crud

from main.crud.form.entry import form_entry_crud

from main.crud.form.entry.answer import (
	form_entry_answer_input_crud,
	form_entry_answer_textarea_crud,
	form_entry_answer_select_crud,
	form_entry_answer_checkbox_crud,
	form_entry_answer_radio_crud,
)

from main.crud.form.question import (
	form_question_input_crud,
	form_question_textarea_crud,
	form_question_select_crud,
	form_question_radio_crud,
)


from main.crud.meta.gs import gs_meta_crud
from main.crud.meta.spng import spng_meta_crud


from main.crud.user import user_crud




