from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting
from plone.app.testing import applyProfile

from zope.configuration import xmlconfig

class PolicyCpasmolenbeek(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE, )

    def setUpZope(self, app, configurationContext):
        # Load ZCML for this package
        import policy.cpasmolenbeek
        xmlconfig.file('configure.zcml',
                       policy.cpasmolenbeek,
                       context=configurationContext)


    def setUpPloneSite(self, portal):
        applyProfile(portal, 'policy.cpasmolenbeek:default')

POLICY_CPASMOLENBEEK_FIXTURE = PolicyCpasmolenbeek()
POLICY_CPASMOLENBEEK_INTEGRATION_TESTING = \
    IntegrationTesting(bases=(POLICY_CPASMOLENBEEK_FIXTURE, ),
                       name="PolicyCpasmolenbeek:Integration")