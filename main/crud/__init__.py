from main.crud._base.resource import resource_base_crud
from main.crud._base.spng_survey import spng_survey_base_crud


from main.crud._many.camp_instances_camp_instance_registrations import camp_instances_camp_instance_registrations_crud
from main.crud._many.camp_instances_coaches import camp_instances_coaches_crud
from main.crud._many.program_instances_coaches import program_instances_coaches_crud
from main.crud._many.program_instances_program_instance_registrations import program_instances_program_instance_registrations_crud
from main.crud._many.team_instances_adult_reps import team_instances_adult_reps_crud
from main.crud._many.team_instances_coaches import team_instances_coaches_crud
from main.crud._many.team_instances_players import team_instances_players_crud
from main.crud._many.team_instances_team_instance_registrations import team_instances_team_instance_registrations_crud
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
# from main.crud.data.camp.instance.registration.invite import camp_instance_registration_invite_crud

from main.crud.data.program import program_crud
from main.crud.data.program.group import program_group_crud
from main.crud.data.program.group.instance import program_group_instance_crud
from main.crud.data.program.instance.registration import program_instance_registration_crud
# from main.crud.data.program.instance.registration.invite import program_instance_registration_invite_crud

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

from main.crud.data.team.instance.order.jersey_socks import team_instance_jersey_socks_order_crud
from main.crud.data.team.instance.order.jersey_socks.group_sheet import team_instance_jersey_socks_order_group_sheet_crud
from main.crud.data.team.instance.order.jersey_socks.request import team_instance_jersey_socks_order_request_crud
from main.crud.data.team.instance.order.jersey_socks.update import team_instance_jersey_socks_order_update_crud

from main.crud.data.team.instance.order.tracksuit import team_instance_tracksuit_order_crud
from main.crud.data.team.instance.order.tracksuit.group_sheet import team_instance_tracksuit_order_group_sheet_crud
from main.crud.data.team.instance.order.tracksuit.request import team_instance_tracksuit_order_request_crud
from main.crud.data.team.instance.order.tracksuit.update import team_instance_tracksuit_order_update_crud

from main.crud.data.team.instance.registration import team_instance_registration_crud
from main.crud.data.team.instance.registration.invite import team_instance_registration_invite_crud
from main.crud.data.team.instance.registration.jersey_sponsor import team_instance_registration_jersey_sponsor_crud

from main.crud.external.spng_survey.camp_instance import spng_survey_camp_instance_crud
from main.crud.external.spng_survey.program_instance import spng_survey_program_instance_crud
from main.crud.external.spng_survey.team_instance import spng_survey_team_instance_crud

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
	form_question_checkbox_crud,
	form_question_radio_crud,
)


from main.crud.meta.gs import gs_meta_crud
from main.crud.meta.spng import spng_meta_crud


from main.crud.resource.category import resource_category_crud

from main.crud.resource.type.article import resource_article_crud
from main.crud.resource.type.pdf import resource_pdf_crud
from main.crud.resource.type.video import resource_video_crud



from main.crud.user import user_crud




