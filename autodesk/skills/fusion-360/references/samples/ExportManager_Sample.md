# ExportManager API Sample

## Description

Demonstrates how to export f3d to different formats.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback
import os.path, sys

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # get active design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # get all components in this design
        allComps = design.allComponents

        # get the script location
        scriptDir = os.path.dirname(os.path.realpath(__file__))

        # create a single exportManager instance
        exportMgr = design.exportManager

        # export the component one by one with a specified format
        for comp in allComps:
            compName = comp.name
            fileName = scriptDir + "/" + compName

            # export the component with IGS format
            igesOptions = exportMgr.createIGESExportOptions(fileName, comp)
            exportMgr.execute(igesOptions)

            # export the component with SAT format
            satOptions = exportMgr.createSATExportOptions(fileName, comp)
            exportMgr.execute(satOptions)

            # export the component with SMT format
            smtOptions = exportMgr.createSMTExportOptions(fileName, comp)
            exportMgr.execute(smtOptions)

            # export the component with STP format
            stpOptions = exportMgr.createSTEPExportOptions(fileName, comp)
            exportMgr.execute(stpOptions)

            # export the component with F3D format
            archOptions = exportMgr.createFusionArchiveExportOptions(fileName, comp)
            exportMgr.execute(archOptions)

             export the component with USD (Universal Scene Description) format
            usdOptions = exportMgr.createUSDExportOptions(fileName, comp)
            exportMgr.execute(usdOptions)
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/Application/Document.h>

#include <Fusion/Fusion/Design.h>
#include <Fusion/Fusion/ExportManager.h>
#include <Fusion/Fusion/ExportOptions.h>
#include <Fusion/Fusion/IGESExportOptions.h>
#include <Fusion/Fusion/FusionArchiveExportOptions.h>
#include <Fusion/Fusion/SATExportOptions.h>
#include <Fusion/Fusion/SMTExportOptions.h>
#include <Fusion/Fusion/STEPExportOptions.h>
#include <Fusion/Components/Components.h>
#include <Fusion/Components/Component.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<UserInterface> ui;

std::string getDllPath();

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    // get active design
    Ptr<Product> product = app->activeProduct();
    if (!product)
        return false;

    Ptr<Design> design = product;
    if (!design)
        return false;

    // get all components in this design
    Ptr<Components> comps = design->allComponents();
    if (!comps)
        return false;

    // create a single exportManager instance
    Ptr<ExportManager> exportMgr = design->exportManager();
    if (!exportMgr)
        return false;

    // export the component one by one with a specified format
    size_t count = comps->count();
    for (size_t index = 0; index < count; ++index)
    {
        Ptr<Component> comp = comps->item(index);
        std::string name = comp->name();
        std::string fileName = getDllPath() + "/" + name;

        // export the component with IGS format
        Ptr<IGESExportOptions> igesOptions = exportMgr->createIGESExportOptions(fileName, comp);
        if (!igesOptions)
            continue;
        exportMgr->execute(igesOptions);

        // export the component with SAT format
        Ptr<SATExportOptions> satOptions = exportMgr->createSATExportOptions(fileName, comp);
        if (!satOptions)
            continue;
        exportMgr->execute(satOptions);

        // export the component with SMT format
        Ptr<SMTExportOptions> smtOptions = exportMgr->createSMTExportOptions(fileName, comp);
        if (!smtOptions)
            continue;
        exportMgr->execute(smtOptions);

        // export the component with STP format
        Ptr<STEPExportOptions> stepOptions = exportMgr->createSTEPExportOptions(fileName, comp);
        if (!stepOptions)
            continue;
        exportMgr->execute(stepOptions);

        // export the component with F3D format
        Ptr<FusionArchiveExportOptions> archOptions = exportMgr->createFusionArchiveExportOptions(fileName, comp);
        if (!stepOptions)
            continue;
        exportMgr->execute(archOptions);
    }

    return true;
}

std::string getDllPath()
{
#if defined(_WINDOWS) || defined(_WIN32) || defined(_WIN64)
    HMODULE hModule = NULL;
    if (!GetModuleHandleExA(
            GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS | GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT,
            (LPCSTR)&getDllPath,
            &hModule))
        return "";

    char winTempPath[2048];
    ::GetModuleFileNameA(hModule, winTempPath, 2048);

    std::string strPath = winTempPath;
    size_t stPos = strPath.rfind('\\');
    return strPath.substr(0, stPos);
#else
    Dl_info info;
    dladdr((void*)getDllPath, &info);

    std::string strPath = info.dli_fname;
    int stPos = (int)strPath.rfind('/');
    if (stPos != -1)
        return strPath.substr(0, stPos);
    else
        return "";
    ;
#endif
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |