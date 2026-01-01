# STLExport API Sample

## Description

Demonstrates how to export f3d to STL format.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback
import os.path

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface

        # get active design
        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # get root component in this design
        rootComp = design.rootComponent

        # create a single exportManager instance
        exportMgr = design.exportManager

        # export the root component to printer utility
        stlRootOptions = exportMgr.createSTLExportOptions(rootComp)

        # get all available print utilities
        printUtils = stlRootOptions.availablePrintUtilities

        # export the root component to the print utility, instead of a specified file
        for printUtil in printUtils:
            stlRootOptions.sendToPrintUtility = True
            stlRootOptions.printUtility = printUtil

            exportMgr.execute(stlRootOptions)

        # get the script location
        scriptDir = os.path.dirname(os.path.realpath(__file__))

        # export the occurrence one by one in the root component to a specified file
        allOccu = rootComp.allOccurrences
        for occ in allOccu:
            fileName = scriptDir + "/" + occ.component.name

            # create stl exportOptions
            stlExportOptions = exportMgr.createSTLExportOptions(occ, fileName)
            stlExportOptions.sendToPrintUtility = False

            exportMgr.execute(stlExportOptions)

        # export the body one by one in the design to a specified file
        allBodies = rootComp.bRepBodies
        for body in allBodies:
            fileName = scriptDir + "/" + body.parentComponent.name + '-' + body.name

            # create stl exportOptions
            stlExportOptions = exportMgr.createSTLExportOptions(body, fileName)
            stlExportOptions.sendToPrintUtility = False

            exportMgr.execute(stlExportOptions)
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
#include <Fusion/Fusion/STLExportOptions.h>
#include <Fusion/Components/Components.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Components/OccurrenceList.h>
#include <Fusion/Components/Occurrence.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepBody.h>

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

    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // create a single exportManager instance
    Ptr<ExportManager> exportMgr = design->exportManager();
    if (!exportMgr)
        return false;

    // export the root component to printer utility
    Ptr<STLExportOptions> stlRootOptions = exportMgr->createSTLExportOptions(rootComp);
    if (!stlRootOptions)
        return false;

    // get all available print utilities
    std::vector<std::string> printUtils = stlRootOptions->availablePrintUtilities();

    // export the root component to the print utility, instead of a specified file
    size_t count = printUtils.size();
    for (size_t i = 0; i < count; i++)
    {
        std::string printUtil = printUtils[i];
        stlRootOptions->sendToPrintUtility(true);
        stlRootOptions->printUtility(printUtil);

        exportMgr->execute(stlRootOptions);
    }

    // export the occurrence one by one in the root component to a specified file
    Ptr<OccurrenceList> occurs = rootComp->allOccurrences();
    if (!occurs)
        return false;
    size_t occrCount = occurs->count();
    for (size_t j = 0; j < occrCount; j++)
    {
        Ptr<Occurrence> occur = occurs->item(j);
        if (!occur)
            continue;

        Ptr<Component> comp = occur->component();
        if (!comp)
            continue;

        std::string compName = comp->name();
        std::string fileName = getDllPath() + "/" + compName;

        // create stl exportOptions
        Ptr<STLExportOptions> stlExportOptions = exportMgr->createSTLExportOptions(occur, fileName);
        stlExportOptions->sendToPrintUtility(false);

        exportMgr->execute(stlExportOptions);
    }

    // export the body one by one in the design to a specified file
    Ptr<BRepBodies> bRepBodies = rootComp->bRepBodies();
    if (!bRepBodies)
        return false;
    size_t bodyCount = bRepBodies->count();
    for (size_t k = 0; k < bodyCount; k++)
    {
        Ptr<BRepBody> body = bRepBodies->item(k);
        if (!body)
            continue;

        Ptr<Component> comp = body->parentComponent();
        if (!comp)
            continue;

        std::string compName = comp->name();
        std::string bodyName = body->name();
        std::string fileName = getDllPath() + "/" + compName + "-" + bodyName;

        // create stl exportOptions
        Ptr<STLExportOptions> stlExportOptions = exportMgr->createSTLExportOptions(body, fileName);
        if (!stlExportOptions)
            continue;

        stlExportOptions->sendToPrintUtility(false);

        exportMgr->execute(stlExportOptions);
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