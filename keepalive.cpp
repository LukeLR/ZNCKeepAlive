#include <znc/Client.h>
#include <znc/Chan.h>
#include <znc/Modules.h>
#include <znc/main.h>

#ifdef HAVE_PTHREAD
class CPingJob : public CModuleJob {
  public:
    CSampleJob(CModule* pModule)
        : CModuleJob(pModule, "ping", "Issue /ping at given intervals") {}

    ~CSampleJob() override {
        if (wasCancelled()) {
            GetModule()->PutModule(GetModule()->t_s("Sample job cancelled"));
        } else {
            GetModule()->PutModule(GetModule()->t_s("Sample job destroyed"));
        }
    }

    void runThread() override {
        // Cannot safely use GetModule() in here, because this runs in its
        // own thread and such an access would require synchronisation
        // between this thread and the main thread!

        for (int i = 0; i < 10; i++) {
            // Regularly check if we were cancelled
            if (wasCancelled()) return;
            sleep(1);
        }
    }

    void runMain() override {
        GetModule()->PutModule(GetModule()->t_s("Sample job done"));
    }
};
#endif
