# Import all the models, so that Base has them before being

from main.database.base_class import Base  # noqa


from main.models._base.registration import RegistrationBaseModel
from main.models._base.resource import ResourceBaseModel
from main.models._base.spng_survey import SpngSurveyBaseModel


from main.models._many.camp_instances_coaches import CampInstancesCoachesModel
from main.models._many.program_instances_coaches import ProgramInstancesCoachesModel
from main.models._many.team_instances_adult_reps import TeamInstancesAdultRepsModel
from main.models._many.team_instances_coaches import TeamInstancesCoachesModel
from main.models._many.team_instances_players import TeamInstancesPlayersModel
from main.models._many.spng_surveys_spng_survey_questions import SpngSurveysSpngSurveyQuestionsModel
from main.models._many.guardians_players import GuardiansPlayersModel


from main.models.data.person.adult_rep import AdultRepModel
from main.models.data.person.coach import CoachModel
from main.models.data.person.guardian import GuardianModel
from main.models.data.person.player import PlayerModel

from main.models.data.camp import CampModel
from main.models.data.camp.group import CampGroupModel
from main.models.data.camp.group.instance import CampGroupInstanceModel
from main.models.data.camp.instance import CampInstanceModel
from main.models.data.camp.instance.registration import CampInstanceRegistrationModel

from main.models.data.program import ProgramModel
from main.models.data.program.group import ProgramGroupModel
from main.models.data.program.group.instance import ProgramGroupInstanceModel
from main.models.data.program.instance import ProgramInstanceModel
from main.models.data.program.instance.registration import ProgramInstanceRegistrationModel

from main.models.data.team import TeamModel
from main.models.data.team.conference import ConferenceModel
from main.models.data.team.division import DivisionModel
from main.models.data.team.league import LeagueModel
from main.models.data.team.season import SeasonModel

from main.models.data.team.instance import TeamInstanceModel
from main.models.data.team.instance.conference import ConferenceInstanceModel
from main.models.data.team.instance.division import DivisionInstanceModel
from main.models.data.team.instance.league import LeagueInstanceModel
from main.models.data.team.instance.season import SeasonInstanceModel

from main.models.data.team.instance.orders.jersey_socks import TeamInstanceJerseySocksOrderModel
from main.models.data.team.instance.orders.tracksuit import TeamInstanceTracksuitOrderModel

from main.models.data.team.instance.registration import TeamInstanceRegistrationModel
from main.models.data.team.instance.registration.jersey_sponsor import TeamInstanceRegistrationJerseySponsorModel

from main.models.external.spng_survey.camp import SpngSurveyCampModel
from main.models.external.spng_survey.program import SpngSurveyProgramModel
from main.models.external.spng_survey.team import SpngSurveyTeamModel

from main.models.external.spng_survey_question import SpngSurveyQuestionModel
from main.models.external.spng_survey_question.table_map import SpngSurveyQuestionTableMapModel

from main.models.form import FormModel

from main.models.form.entry import FormEntryModel

from main.models.form.entry.answer import (
	FormEntryAnswerModel,
	FormEntryAnswerInputModel,
	FormEntryAnswerTextareaModel,
	FormEntryAnswerSelectModel,
	FormEntryAnswerCheckboxModel,
	FormEntryAnswerRadioModel,
)

from main.models.form.question import (
	FormQuestionModel,
	FormQuestionInputModel,
	FormQuestionTextareaModel,
	FormQuestionSelectModel,
	FormQuestionCheckboxModel,
	FormQuestionRadioModel,
)

from main.models.meta.gs import GSMetaModel
from main.models.meta.spng import SpngMetaModel

from main.models.resource.category import ResourceCategoryModel

from main.models.resource.type.article import ResourceArticleModel
from main.models.resource.type.pdf import ResourcePDFModel
from main.models.resource.type.video import ResourceVideoModel


from main.models.user import UserModel


print(';;;;')
print(Base.metadata.tables.keys())


# Explicity set up mappers. -- AbstractConcreteBase ...
from sqlalchemy.orm import configure_mappers
configure_mappers()



