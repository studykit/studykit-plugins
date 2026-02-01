# Construction Axis API Sample

## Description

Demonstrates creating construction axis in various ways.

## Code Samples

* [Python](#Python)
* [C++](#C++)

|  |
| --- |
| Copy Code |

```
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface

        # Create a document.
        doc = app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)

        product = app.activeProduct
        design = adsk.fusion.Design.cast(product)

        # Get the root component of the active design
        rootComp = design.rootComponent

        # Create sketch
        sketches = rootComp.sketches
        sketch = sketches.add(rootComp.xZConstructionPlane)
        sketchCircles = sketch.sketchCurves.sketchCircles
        centerPoint = adsk.core.Point3D.create(0, 0, 0)
        sketchCircles.addByCenterRadius(centerPoint, 5.0)

        sketchLines = sketch.sketchCurves.sketchLines
        sketchLines.addTwoPointRectangle(adsk.core.Point3D.create(6, 6, 0), adsk.core.Point3D.create(-6, -6, 0))

        # Get the profile defined by the circle
        prof = sketch.profiles.item(1)

        # Create an extrusion input
        extrudes = rootComp.features.extrudeFeatures
        extInput = extrudes.createInput(prof, adsk.fusion.FeatureOperations.NewBodyFeatureOperation)

        # Define that the extent is a distance extent of 5 cm
        distance = adsk.core.ValueInput.createByReal(5)
        # Set the distance extent to be symmetric
        extInput.setDistanceExtent(True, distance)
        # Set the extrude to be a solid one
        extInput.isSolid = True

        # Create the extrusion
        ext = extrudes.add(extInput)

        # Get the body created by the extrusion
        body = ext.bodies.item(0)

        axes = rootComp.constructionAxes
        axisInput = axes.createInput()

        # Add by line
        if design.designType == adsk.fusion.DesignTypes.DirectDesignType:
            axisInput.setByLine(adsk.core.InfiniteLine3D.create(adsk.core.Point3D.create(0), adsk.core.Vector3D.create(1, 0, 0)))
            axes.add(axisInput)

        # Prepare reference data
        circularFace = None
        for face in body.faces:
            geom = face.geometry
            if geom.surfaceType == adsk.core.SurfaceTypes.CylinderSurfaceType:
                circularFace = face
                break

        linearEdge = None
        for edge in body.edges:
            edgeGeom = edge.geometry
            if edgeGeom.curveType == adsk.core.Curve3DTypes.Line3DCurveType:
                linearEdge = edge
                break

        faceOne = linearEdge.faces.item(0)
        faceTwo = linearEdge.faces.item(1)
        vertexOne = faceOne.vertices.item(0)
        vertexTwo = faceOne.vertices.item(1)

        # Add by circularFace
        axisInput.setByCircularFace(circularFace)
        axes.add(axisInput)

        # Add by perpendicular at point
        axisInput.setByPerpendicularAtPoint(faceOne, vertexOne)
        axes.add(axisInput)

        # Add by two planes
        axisInput.setByTwoPlanes(faceOne, faceTwo)
        axes.add(axisInput)

        # Add by two points
        axisInput.setByTwoPoints(vertexOne, vertexTwo)
        axes.add(axisInput)

        # Add by edge
        axisInput.setByEdge(linearEdge)
        axes.add(axisInput)

        # Add by normal to face at point
        axisInput.setByNormalToFaceAtPoint(faceTwo, vertexOne)
        axis = axes.add(axisInput)

        # Get health state of the axis
        health = axis.healthState
        if health == adsk.fusion.FeatureHealthStates.WarningFeatureHealthState or health == adsk.fusion.FeatureHealthStates.ErrorFeatureHealthState:
            message = axis.errorOrWarningMessage
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
#include <Core/Application/ValueInput.h>
#include <Core/Geometry/Point3D.h>
#include <Core/Geometry/InfiniteLine3D.h>
#include <Core/Geometry/Line3D.h>
#include <Core/Geometry/Surface.h>
#include <Core/Geometry/Vector3D.h>
#include <Core/UserInterface/UserInterface.h>
#include <Fusion/BRep/BRepBody.h>
#include <Fusion/BRep/BRepBodies.h>
#include <Fusion/BRep/BRepEdge.h>
#include <Fusion/BRep/BRepEdges.h>
#include <Fusion/BRep/BRepFace.h>
#include <Fusion/BRep/BRepFaces.h>
#include <Fusion/BRep/BRepVertices.h>
#include <Fusion/BRep/BRepVertex.h>
#include <Fusion/Components/Component.h>
#include <Fusion/Construction/ConstructionAxes.h>
#include <Fusion/Construction/ConstructionAxis.h>
#include <Fusion/Construction/ConstructionAxisInput.h>
#include <Fusion/Construction/ConstructionPlane.h>
#include <Fusion/Features/Features.h>
#include <Fusion/Features/ExtrudeFeature.h>
#include <Fusion/Features/ExtrudeFeatures.h>
#include <Fusion/Features/ExtrudeFeatureInput.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Sketch/Profile.h>
#include <Fusion/Sketch/Profiles.h>
#include <Fusion/Sketch/Sketch.h>
#include <Fusion/Sketch/Sketches.h>
#include <Fusion/Sketch/SketchCircle.h>
#include <Fusion/Sketch/SketchCircles.h>
#include <Fusion/Sketch/SketchCurves.h>
#include <Fusion/Sketch/SketchLine.h>
#include <Fusion/Sketch/SketchLines.h>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    Ptr<Documents> documents = app->documents();
    if (!documents)
        return false;

    Ptr<Document> doc = documents->add(DocumentTypes::FusionDesignDocumentType);
    if (!doc)
        return false;

    Ptr<Product> product = app->activeProduct();
    if (!product)
        return false;

    Ptr<Design> design = product;
    if (!design)
        return false;

    // Get the root component of the active design
    Ptr<Component> rootComp = design->rootComponent();
    if (!rootComp)
        return false;

    // Create sketch
    Ptr<Sketches> sketches = rootComp->sketches();
    if (!sketches)
        return false;
    Ptr<ConstructionPlane> xz = rootComp->xZConstructionPlane();
    if (!xz)
        return false;
    Ptr<Sketch> sketch = sketches->add(xz);
    if (!sketch)
        return false;
    Ptr<SketchCurves> sketchCurves = sketch->sketchCurves();
    if (!sketchCurves)
        return false;
    Ptr<SketchCircles> sketchCircles = sketchCurves->sketchCircles();
    if (!sketchCircles)
        return false;
    Ptr<Point3D> centerPoint = Point3D::create(0, 0, 0);
    if (!centerPoint)
        return false;
    Ptr<SketchCircle> circle = sketchCircles->addByCenterRadius(centerPoint, 5.0);
    if (!circle)
        return false;

    Ptr<SketchLines> sketchLines = sketchCurves->sketchLines();
    if (!sketchLines)
        return false;
    sketchLines->addTwoPointRectangle(Point3D::create(6, 6, 0), Point3D::create(-6, -6, 0));

    // Get the profile defined by the circle
    Ptr<Profiles> profs = sketch->profiles();
    if (!profs)
        return false;
    Ptr<Profile> prof = profs->item(1);
    if (!prof)
        return false;

    // Create an extrusion input
    Ptr<Features> feats = rootComp->features();
    if (!feats)
        return false;
    Ptr<ExtrudeFeatures> extrudes = feats->extrudeFeatures();
    if (!extrudes)
        return false;
    Ptr<ExtrudeFeatureInput> extInput = extrudes->createInput(prof, FeatureOperations::NewBodyFeatureOperation);
    if (!extInput)
        return false;

    // Define that the extent is a distance extent of 5 cm
    Ptr<ValueInput> distance = ValueInput::createByReal(5);
    if (!distance)
        return false;
    // Set the distance extent to be symmetric
    extInput->setDistanceExtent(true, distance);
    // Set the extrude to be a solid one
    extInput->isSolid(true);

    // Create the extrusion
    Ptr<ExtrudeFeature> ext = extrudes->add(extInput);
    if (!ext)
        return false;

    // Get the body created by the extrusion
    Ptr<BRepBodies> bodies = ext->bodies();
    if (!bodies)
        return false;
    Ptr<BRepBody> body = bodies->item(0);
    if (!body)
        return false;

    Ptr<ConstructionAxes> axes = rootComp->constructionAxes();
    if (!axes)
        return false;

    Ptr<ConstructionAxisInput> axisInput = axes->createInput();
    if (!axisInput)
        return false;

    // Add by line
    if (design->designType() == DesignTypes::DirectDesignType)
    {
        axisInput->setByLine(InfiniteLine3D::create(Point3D::create(0), Vector3D::create(1, 0, 0)));
        axes->add(axisInput);
    }

    Ptr<BRepFaces> faces = body->faces();
    if (!faces)
        return false;

    // Prepare reference data
    Ptr<BRepFace> circularFace = nullptr;
    for (auto face : faces)
    {
        Ptr<Surface> geom = face->geometry();
        if (geom->surfaceType() == SurfaceTypes::CylinderSurfaceType)
        {
            circularFace = face;
            break;
        }
    }

    Ptr<BRepEdge> linearEdge = nullptr;
    for (auto edge : body->edges())
    {
        Ptr<Curve3D> edgeGeom = edge->geometry();
        if (edgeGeom->curveType() == Curve3DTypes::Line3DCurveType)
        {
            linearEdge = edge;
            break;
        }
    }

    Ptr<BRepFace> faceOne = faces->item(0);
    if (!faceOne)
        return false;

    Ptr<BRepFace> faceTwo = faces->item(1);
    if (!faceTwo)
        return false;

    Ptr<BRepVertices> vertices = faceOne->vertices();
    if (!vertices)
        return false;

    Ptr<BRepVertex> vertexOne = vertices->item(0);
    if (!vertexOne)
        return false;

    Ptr<BRepVertex> vertexTwo = vertices->item(1);
    if (!vertexTwo)
        return false;

    // Add by circularFace
    axisInput->setByCircularFace(circularFace);
    axes->add(axisInput);

    // Add by perpendicular at point
    axisInput->setByPerpendicularAtPoint(faceOne, vertexOne);
    axes->add(axisInput);

    // Add by two planes
    axisInput->setByTwoPlanes(faceOne, faceTwo);
    axes->add(axisInput);

    // Add by two points
    axisInput->setByTwoPoints(vertexOne, vertexTwo);
    axes->add(axisInput);

    // Add by edge
    axisInput->setByEdge(linearEdge);
    axes->add(axisInput);

    // Add by normal to face at point
    axisInput->setByNormalToFaceAtPoint(faceTwo, vertexOne);
    Ptr<ConstructionAxis> axis = axes->add(axisInput);

    // Get the health state of a construction plane
    adsk::fusion::FeatureHealthStates health = axis->healthState();
    if (health == adsk::fusion::FeatureHealthStates::ErrorFeatureHealthState ||
        health == adsk::fusion::FeatureHealthStates::WarningFeatureHealthState)
    {
        std::string msg = axis->errorOrWarningMessage();
    }

    return true;
}
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |