from main.schemas._base.registration import (
	RegistrationBaseSchemaBase,
)
from main.schemas._base.spng_survey import (
	SpngSurveyBaseSchemaCreate,
	SpngSurveyBaseSchemaUpdate,
	SpngSurveyBaseSchema,
	SpngSurveyBaseSchemaInDB,
)


from main.schemas._many.camp_instances_coaches import (
	CampInstancesCoachesSchemaCreate,
	CampInstancesCoachesSchemaUpdate,
	CampInstancesCoachesSchema,
	CampInstancesCoachesSchemaInDB,
)
from main.schemas._many.program_instances_coaches import (
	ProgramInstancesCoachesSchemaCreate,
	ProgramInstancesCoachesSchemaUpdate,
	ProgramInstancesCoachesSchema,
	ProgramInstancesCoachesSchemaInDB,
)
from main.schemas._many.team_instances_adult_reps import (
	TeamInstancesAdultRepsSchemaCreate,
	TeamInstancesAdultRepsSchemaUpdate,
	TeamInstancesAdultRepsSchema,
	TeamInstancesAdultRepsSchemaInDB,
)
from main.schemas._many.team_instances_coaches import (
	TeamInstancesCoachesSchemaCreate,
	TeamInstancesCoachesSchemaUpdate,
	TeamInstancesCoachesSchema,
	TeamInstancesCoachesSchemaInDB,
)
from main.schemas._many.team_instances_players import (
	TeamInstancesPlayersSchemaCreate,
	TeamInstancesPlayersSchemaUpdate,
	TeamInstancesPlayersSchema,
	TeamInstancesPlayersSchemaInDB,
)
from main.schemas._many.spng_surveys_spng_survey_questions import (
	SpngSurveysSpngSurveyQuestionsSchemaCreate,
	SpngSurveysSpngSurveyQuestionsSchemaUpdate,
	SpngSurveysSpngSurveyQuestionsSchema,
	SpngSurveysSpngSurveyQuestionsSchemaInDB,
)
from main.schemas._many.guardians_players import (
	GuardiansPlayersSchemaCreate,
	GuardiansPlayersSchemaUpdate,
	GuardiansPlayersSchema,
	GuardiansPlayersSchemaInDB,
)


from main.schemas.data.person.coach import (
	CoachSchemaCreate,
	CoachSchemaUpdate,
	CoachSchema,
	CoachSchemaInDB,
)
from main.schemas.data.person.guardian import (
	GuardianSchemaCreate,
	GuardianSchemaUpdate,
	GuardianSchema,
	GuardianSchemaInDB,
)
from main.schemas.data.person.player import (
	PlayerSchemaCreate,
	PlayerSchemaUpdate,
	PlayerSchema,
	PlayerSchemaInDB,
)

from main.schemas.data.camp import (
	CampSchemaCreate,
	CampSchemaUpdate,
	CampSchema,
	CampSchemaInDB,
)
from main.schemas.data.camp.group import (
	CampGroupSchemaCreate,
	CampGroupSchemaUpdate,
	CampGroupSchema,
	CampGroupSchemaInDB,
)
from main.schemas.data.camp.group.instance import (
	CampGroupInstanceSchemaCreate,
	CampGroupInstanceSchemaUpdate,
	CampGroupInstanceSchema,
	CampGroupInstanceSchemaInDB,
)
from main.schemas.data.camp.instance import (
	CampInstanceSchemaCreate,
	CampInstanceSchemaUpdate,
	CampInstanceSchema,
	CampInstanceSchemaInDB,
)
from main.schemas.data.camp.instance.registration import (
	CampInstanceRegistrationSchemaCreate,
	CampInstanceRegistrationSchemaUpdate,
	CampInstanceRegistrationSchema,
	CampInstanceRegistrationSchemaInDB,
)

from main.schemas.data.program import (
	ProgramSchemaCreate,
	ProgramSchemaUpdate,
	ProgramSchema,
	ProgramSchemaInDB,
)
from main.schemas.data.program.group import (
	ProgramGroupSchemaCreate,
	ProgramGroupSchemaUpdate,
	ProgramGroupSchema,
	ProgramGroupSchemaInDB,
)
from main.schemas.data.program.group.instance import (
	ProgramGroupInstanceSchemaCreate,
	ProgramGroupInstanceSchemaUpdate,
	ProgramGroupInstanceSchema,
	ProgramGroupInstanceSchemaInDB,
)
from main.schemas.data.program.instance import (
	ProgramInstanceSchemaCreate,
	ProgramInstanceSchemaUpdate,
	ProgramInstanceSchema,
	ProgramInstanceSchemaInDB,
)
from main.schemas.data.program.instance.registration import (
	ProgramInstanceRegistrationSchemaCreate,
	ProgramInstanceRegistrationSchemaUpdate,
	ProgramInstanceRegistrationSchema,
	ProgramInstanceRegistrationSchemaInDB,
)

from main.schemas.data.team import (
	TeamSchemaCreate,
	TeamSchemaUpdate,
	TeamSchema,
	TeamSchemaInDB,
)
from main.schemas.data.team.conference import (
	ConferenceSchemaCreate,
	ConferenceSchemaUpdate,
	ConferenceSchema,
	ConferenceSchemaInDB,
)
from main.schemas.data.team.division import (
	DivisionSchemaCreate,
	DivisionSchemaUpdate,
	DivisionSchema,
	DivisionSchemaInDB,
)
from main.schemas.data.team.league import (
	LeagueSchemaCreate,
	LeagueSchemaUpdate,
	LeagueSchema,
	LeagueSchemaInDB,
)
from main.schemas.data.team.season import (
	SeasonSchemaCreate,
	SeasonSchemaUpdate,
	SeasonSchema,
	SeasonSchemaInDB,
)

from main.schemas.data.team.instance import (
	TeamInstanceSchemaCreate,
	TeamInstanceSchemaUpdate,
	TeamInstanceSchema,
	TeamInstanceSchemaInDB,
)
from main.schemas.data.team.instance.conference import (
	ConferenceInstanceSchemaCreate,
	ConferenceInstanceSchemaUpdate,
	ConferenceInstanceSchema,
	ConferenceInstanceSchemaInDB,
)
from main.schemas.data.team.instance.division import (
	DivisionInstanceSchemaCreate,
	DivisionInstanceSchemaUpdate,
	DivisionInstanceSchema,
	DivisionInstanceSchemaInDB,
)
from main.schemas.data.team.instance.league import (
	LeagueInstanceSchemaCreate,
	LeagueInstanceSchemaUpdate,
	LeagueInstanceSchema,
	LeagueInstanceSchemaInDB,
)
from main.schemas.data.team.instance.season import (
	SeasonInstanceSchemaCreate,
	SeasonInstanceSchemaUpdate,
	SeasonInstanceSchema,
	SeasonInstanceSchemaInDB,
)

from main.schemas.data.team.instance.order.jersey_socks import (
	TeamInstanceJerseySocksOrderSchemaCreate,
	TeamInstanceJerseySocksOrderSchemaUpdate,
	TeamInstanceJerseySocksOrderSchema,
	TeamInstanceJerseySocksOrderSchemaInDB,
)
from main.schemas.data.team.instance.order.tracksuit import (
	TeamInstanceTracksuitOrderSchemaCreate,
	TeamInstanceTracksuitOrderSchemaUpdate,
	TeamInstanceTracksuitOrderSchema,
	TeamInstanceTracksuitOrderSchemaInDB,
)

from main.schemas.data.team.instance.registration import (
	TeamInstanceRegistrationSchemaCreate,
	TeamInstanceRegistrationSchemaUpdate,
	TeamInstanceRegistrationSchema,
	TeamInstanceRegistrationSchemaInDB,
)
from main.schemas.data.team.instance.registration.jersey_sponsor import (
	TeamInstanceRegistrationJerseySponsorSchemaCreate,
	TeamInstanceRegistrationJerseySponsorSchemaUpdate,
	TeamInstanceRegistrationJerseySponsorSchema,
	TeamInstanceRegistrationJerseySponsorSchemaInDB,
)

from main.schemas.external.spng_survey.camp_instance import (
	SpngSurveyCampInstanceSchemaCreate,
	SpngSurveyCampInstanceSchemaUpdate,
	SpngSurveyCampInstanceSchema,
	SpngSurveyCampInstanceSchemaInDB,
)
from main.schemas.external.spng_survey.program_instance import (
	SpngSurveyProgramInstanceSchemaCreate,
	SpngSurveyProgramInstanceSchemaUpdate,
	SpngSurveyProgramInstanceSchema,
	SpngSurveyProgramInstanceSchemaInDB,
)
from main.schemas.external.spng_survey.team_instance import (
	SpngSurveyTeamInstanceSchemaCreate,
	SpngSurveyTeamInstanceSchemaUpdate,
	SpngSurveyTeamInstanceSchema,
	SpngSurveyTeamInstanceSchemaInDB,
)

from main.schemas.external.spng_survey_question import (
	SpngSurveyQuestionSchemaCreate,
	SpngSurveyQuestionSchemaUpdate,
	SpngSurveyQuestionSchema,
	SpngSurveyQuestionSchemaInDB,
)
from main.schemas.external.spng_survey_question.table_map import (
	SpngSurveyQuestionTableMapSchemaCreate,
	SpngSurveyQuestionTableMapSchemaUpdate,
	SpngSurveyQuestionTableMapSchema,
	SpngSurveyQuestionTableMapSchemaInDB,
)

from main.schemas.form import (
	FormSchemaCreate,
	FormSchemaUpdate,
	FormSchema,
	FormSchemaInDB,
)

from main.schemas.form.entry import (
	FormEntrySchemaCreate,
	FormEntrySchemaUpdate,
	FormEntrySchema,
	FormEntrySchemaInDB,
)

from main.schemas.form.entry.answer import (
	FormEntryAnswerSchemaCreate,
	FormEntryAnswerSchemaUpdate,
	FormEntryAnswerSchema,
	FormEntryAnswerSchemaInDB,

	# Inherited --

	FormEntryAnswerInputSchemaCreate,
	FormEntryAnswerInputSchemaUpdate,
	FormEntryAnswerInputSchema,
	FormEntryAnswerInputSchemaInDB,

	FormEntryAnswerTextareaSchemaCreate,
	FormEntryAnswerTextareaSchemaUpdate,
	FormEntryAnswerTextareaSchema,
	FormEntryAnswerTextareaSchemaInDB,

	FormEntryAnswerSelectSchemaCreate,
	FormEntryAnswerSelectSchemaUpdate,
	FormEntryAnswerSelectSchema,
	FormEntryAnswerSelectSchemaInDB,

	FormEntryAnswerCheckboxSchemaCreate,
	FormEntryAnswerCheckboxSchemaUpdate,
	FormEntryAnswerCheckboxSchema,
	FormEntryAnswerCheckboxSchemaInDB,

	FormEntryAnswerRadioSchemaCreate,
	FormEntryAnswerRadioSchemaUpdate,
	FormEntryAnswerRadioSchema,
	FormEntryAnswerRadioSchemaInDB,

)


from main.schemas.form.question import (
	FormQuestionSchemaCreate,
	FormQuestionSchemaUpdate,
	FormQuestionSchema,
	FormQuestionSchemaInDB,

	# Inherited --

	FormQuestionInputSchemaCreate,
	FormQuestionInputSchemaUpdate,
	FormQuestionInputSchema,
	FormQuestionInputSchemaInDB,

	FormQuestionTextareaSchemaCreate,
	FormQuestionTextareaSchemaUpdate,
	FormQuestionTextareaSchema,
	FormQuestionTextareaSchemaInDB,

	FormQuestionSelectSchemaCreate,
	FormQuestionSelectSchemaUpdate,
	FormQuestionSelectSchema,
	FormQuestionSelectSchemaInDB,

	FormQuestionCheckboxSchemaCreate,
	FormQuestionCheckboxSchemaUpdate,
	FormQuestionCheckboxSchema,
	FormQuestionCheckboxSchemaInDB,

	FormQuestionRadioSchemaCreate,
	FormQuestionRadioSchemaUpdate,
	FormQuestionRadioSchema,
	FormQuestionRadioSchemaInDB,

)


from main.schemas.meta.gs import (
	GSMetaSchemaCreate,
	GSMetaSchemaUpdate,
	GSMetaSchema,
	GSMetaSchemaInDB,
)
from main.schemas.meta.spng import (
	SpngMetaSchemaCreate,
	SpngMetaSchemaUpdate,
	SpngMetaSchema,
	SpngMetaSchemaInDB,
)


from main.schemas.resource.category import (
	ResourceCategorySchemaCreate,
	ResourceCategorySchemaUpdate,
	ResourceCategorySchema,
	ResourceCategorySchemaInDB,
)

from main.schemas.resource.type.article import (
	ResourceArticleSchemaCreate,
	ResourceArticleSchemaUpdate,
	ResourceArticleSchema,
	ResourceArticleSchemaInDB,
)
from main.schemas.resource.type.pdf import (
	ResourcePDFSchemaCreate,
	ResourcePDFSchemaUpdate,
	ResourcePDFSchema,
	ResourcePDFSchemaInDB,
)
from main.schemas.resource.type.video import (
	ResourceVideoSchemaCreate,
	ResourceVideoSchemaUpdate,
	ResourceVideoSchema,
	ResourceVideoSchemaInDB,
)


from main.schemas.user import (
	UserSchemaCreate,
	UserSchemaUpdate,
	UserSchema,
	UserSchemaInDB,
)


