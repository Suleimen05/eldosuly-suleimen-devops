import hudson.plugins.git.GitSCM
import hudson.security.FullControlOnceLoggedInAuthorizationStrategy
import hudson.security.HudsonPrivateSecurityRealm
import jenkins.model.Jenkins
import org.jenkinsci.plugins.workflow.cps.CpsScmFlowDefinition
import org.jenkinsci.plugins.workflow.job.WorkflowJob

def jenkins = Jenkins.get()
def adminName = System.getenv('JENKINS_ADMIN_USER')
def adminPassword = System.getenv('JENKINS_ADMIN_PASSWORD')

if (!adminName || !adminPassword) {
    throw new IllegalStateException('Set Jenkins admin credentials before starting')
}

if (!(jenkins.securityRealm instanceof HudsonPrivateSecurityRealm)) {
    def realm = new HudsonPrivateSecurityRealm(false)
    realm.createAccount(adminName, adminPassword)
    jenkins.setSecurityRealm(realm)

    def authorization = new FullControlOnceLoggedInAuthorizationStrategy()
    authorization.setAllowAnonymousRead(false)
    jenkins.setAuthorizationStrategy(authorization)
    jenkins.save()
}

def jobName = 'Eldosuly_Suleimen_DevOps'
def job = jenkins.getItem(jobName)
if (job == null) {
    job = jenkins.createProject(WorkflowJob, jobName)
}

def source = new GitSCM('https://github.com/Suleimen05/eldosuly-suleimen-devops.git')
source.branches = [new hudson.plugins.git.BranchSpec('*/main')]
job.setDefinition(new CpsScmFlowDefinition(source, 'Jenkinsfile'))
job.save()
