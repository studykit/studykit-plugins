# Export to other formats API Sample

## Description

Demonstrates exporting the active design to IGES, STEP, SAT, SMT, F3D and STL formats. To run this sample, have a design open and run the script. It will write out the translated files to a temp directory, which will it show in a message box.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback, tempfile

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui  = app.userInterface
        design = app.activeProduct
        # Get the ExportManager from the active design.
        exportMgr = design.exportManager

        tmpDir = tempfile.gettempdir()

        # Create an IgesExportOptions object and do the export.
        igesOptions = exportMgr.createIGESExportOptions(tmpDir + '/test.igs')
        res = exportMgr.execute(igesOptions)

        # Create an STEPExportOptions object and do the export.
        stepOptions = exportMgr.createSTEPExportOptions(tmpDir+ '/test.step')
        res = exportMgr.execute(stepOptions)

        # Create a SATExportOptions object and do the export.
        satOptions = exportMgr.createSATExportOptions(tmpDir + '/test.sat')
        res = exportMgr.execute(satOptions)

        # Create a SMTExportOptions object and do the export.
        smtOptions = exportMgr.createSMTExportOptions(tmpDir + '/test.smt')
        res = exportMgr.execute(smtOptions)

        # Create a FusionArchiveExportOptions object and do the export.
        fusionArchivevOptions = exportMgr.createFusionArchiveExportOptions(tmpDir + '/test.f3d')
        res = exportMgr.execute(fusionArchivevOptions)
        ui.messageBox(f'Design exported to: {tmpDir}')
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Application/Documents.h>
#include <Core/Application/Document.h>
#include <Core/Application/Product.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/Geometry/Point3D.h>

#include <Fusion/Fusion/Design.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/FusionTypeDefs.h>
#include <Fusion/Fusion/ExportManager.h>
#include <Fusion/Fusion/ExportOptions.h>
#include <Fusion/Fusion/IGESExportOptions.h>
#include <Fusion/Fusion/FusionArchiveExportOptions.h>
#include <Fusion/Fusion/SATExportOptions.h>
#include <Fusion/Fusion/SMTExportOptions.h>
#include <Fusion/Fusion/STEPExportOptions.h>
#include <Fusion/Fusion/STLExportOptions.h>

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

    Ptr<Product> product = app->activeProduct();
    if (!product)
        return false;

    Ptr<Design> design = product;
    if (!design)
        return false;

    Ptr<ExportManager> exportMgr = design->exportManager();
    if (!exportMgr)
        return false;

    std::string pathName = getDllPath();
    Ptr<IGESExportOptions> igesOptions = exportMgr->createIGESExportOptions(pathName + "/" + "test.igs");
    if (!igesOptions)
        return false;
    bRet = exportMgr->execute(igesOptions);

    Ptr<STEPExportOptions> stepOptions = exportMgr->createSTEPExportOptions(pathName + "/" + "test.step");
    if (!stepOptions)
        return false;
    bRet = exportMgr->execute(stepOptions);

    Ptr<SATExportOptions> satOptions = exportMgr->createSATExportOptions(pathName + "/" + "test.sat");
    if (!satOptions)
        return false;
    bRet = exportMgr->execute(satOptions);

    Ptr<SMTExportOptions> smtOptions = exportMgr->createSMTExportOptions(pathName + "/" + "test.smt");
    if (!smtOptions)
        return false;
    bRet = exportMgr->execute(smtOptions);

    Ptr<FusionArchiveExportOptions> fusionArchiveOptions =
        exportMgr->createFusionArchiveExportOptions(pathName + "/" + "test.f3d");
    if (!fusionArchiveOptions)
        return false;
    bRet = exportMgr->execute(fusionArchiveOptions);

    Ptr<STLExportOptions> stlOptions = exportMgr->createSTLExportOptions(rootComp, pathName + "/" + "test.stl");
    if (!stlOptions)
        return false;
    stlOptions->isBinaryFormat(true);
    stlOptions->meshRefinement(MeshRefinementHigh);
    bRet = exportMgr->execute(stlOptions);

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