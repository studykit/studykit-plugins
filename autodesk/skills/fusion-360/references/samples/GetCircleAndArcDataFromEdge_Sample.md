# Get Circle and Arc Data from Edge API Sample

## Description

Display the arc and circle geometric information from a selected circular edge.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback

def getArcGeometryInfo(arcGeom):
    result = arcGeom.getData()
    if (result[0]):
        (retVal, center, axis, refVector, radius, startAngle, endAngle) = result

        arcInfo = "Center: %.6f, %.6f, %.6f\n" % (center.x, center.y, center.z)
        arcInfo += "Axis: %.6f, %.6f, %.6f\n" % (axis.x, axis.y, axis.z)
        arcInfo += "Reference vector: %.6f, %.6f, %.6f\n" % (refVector.x, refVector.y, refVector.z)
        arcInfo += "Radius: %.6f\n" % radius
        arcInfo += "Start angle: %.6f\n" % startAngle
        arcInfo += "End angle: %.6f" % endAngle
        return arcInfo

def getCircleGeometryInfo(circGeom):
    result = circGeom.getData()
    if (result[0]):
        (retVal, center, axis, radius) = result

        circleInfo = "Center: %.6f, %.6f, %.6f\n" % (center.x, center.y, center.z)
        circleInfo += "Axis: %.6f, %.6f, %.6f\n" % (axis.x, axis.y, axis.z)
        circleInfo += "Radius: %.6f" % radius
        return circleInfo

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        ent = ui.selectEntity("Select a circular edge", "CircularEdges")

        if (isinstance(ent.entity.geometry, adsk.core.Arc3D)):
            arcGeom = ent.entity.geometry

            arcInfo = getArcGeometryInfo(arcGeom)

            ui.messageBox(arcInfo, "Arc Info")
        else:
            if (isinstance(ent.entity.geometry, adsk.core.Circle3D)):
                circGeom = ent.entity.geometry

                circleInfo = getCircleGeometryInfo(circGeom)

                ui.messageBox( circleInfo, "Circle Info")
    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/Geometry/Arc3D.h>
#include <Core/Geometry/Circle3D.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/Vector3D.h>
#include <Core/UserInterface/Selection.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepEdge.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<UserInterface> ui;

namespace
{
std::string getArcGeometryInfo(Ptr<Arc3D> arcGeom)
{
    std::string arcInfo;
    if (!arcGeom)
        return arcInfo;

    Ptr<Point3D> center;
    Ptr<Vector3D> axis;
    Ptr<Vector3D> refVector;
    double radius = 0.0;
    double startAngle = 0.0;
    double endAngle = 0.0;
    bool result = arcGeom->getData(center, axis, refVector, radius, startAngle, endAngle);
    if (!result)
        return arcInfo;

    std::stringstream ss;
    ss.precision(6);
    ss << std::fixed;
    ss << "Center: " << center->x() << ", " << center->y() << ", " << center->z() << "\n";
    ss << "Axis: " << axis->x() << ", " << axis->y() << ", " << axis->z() << "\n";
    ss << "Reference vector: " << refVector->x() << ", " << refVector->y() << ", " << refVector->z() << "\n";
    ss << "Radius: " << radius << "\n";
    ss << "Start angle: " << startAngle << "\n";
    ss << "End angle: " << endAngle << "\n";

    arcInfo += ss.str();
    return arcInfo;
}

std::string getCircleGeometryInfo(Ptr<Circle3D> circGeom)
{
    std::string circleInfo;
    if (!circGeom)
        return circleInfo;

    Ptr<Point3D> center;
    Ptr<Vector3D> axis;
    double radius = 0.0;
    bool result = circGeom->getData(center, axis, radius);
    if (!result)
        return circleInfo;

    std::stringstream ss;
    ss.precision(6);
    ss << std::fixed;
    ss << "Center: " << center->x() << ", " << center->y() << ", " << center->z() << "\n";
    ss << "Axis: " << axis->x() << ", " << axis->y() << ", " << axis->z() << "\n";
    ss << "Radius: " << radius << "\n";

    circleInfo += ss.str();
    return circleInfo;
}
} // namespace

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

     Ptr<Selection> selection = ui->selectEntity("Select a circular edge", "CircularEdges");
     if (!selection)
    	return false;

     Ptr<BRepEdge> edge = selection->entity();
     if (!edge)
    	return false;

     if (Ptr<Arc3D> arcGeom = edge->geometry()) {
    	std::string arcInfo = getArcGeometryInfo(arcGeom);
    	ui->messageBox(arcInfo, "Arc Info");
     }
     else if (Ptr<Circle3D> circGeom = edge->geometry()) {
    	std::string circleInfo = getCircleGeometryInfo(circGeom);
    	ui->messageBox(circleInfo, "Circle Info");
     }

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |