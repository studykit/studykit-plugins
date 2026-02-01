# Point3D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Point3D.h>

## Description

Transient 3D point. A transient point is not displayed or saved in a document. Transient 3D points are used as a wrapper to work with raw 3D point information. They are created statically using the create method of the Point3D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [asArray](Point3D_asArray.htm) | Get coordinate data of the point. |
| [asVector](Point3D_asVector.htm) | Defines a vector using the coordinates of the point. |
| [classType](Point3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Point3D_copy.htm) | Creates and returns a copy of this point object. |
| [create](Point3D_create.htm) | Creates a transient 3D point object. |
| [distanceTo](Point3D_distanceTo.htm) | Returns the distance from this point to another point. |
| [getData](Point3D_getData.htm) | Gets the data defining the point. |
| [isEqualTo](Point3D_isEqualTo.htm) | Checks to see if this point and another point are equal (have identical coordinates). The comparison is done within the modeling tolerance which can be found with the Application.pointTolerance property. If you want to compare two points with any other tolerance you can use the isEqualToByTolerance method. |
| [isEqualToByTolerance](Point3D_isEqualToByTolerance.htm) | Checks to see if this point and another point are equal within the specified tolerance. |
| [set](Point3D_set.htm) | Sets the data defining the point. |
| [setWithArray](Point3D_setWithArray.htm) | Sets the coordinates of the point using an array as input. |
| [transformBy](Point3D_transformBy.htm) | Transforms the point using the provided matrix. |
| [translateBy](Point3D_translateBy.htm) | Translates the point using the provided vector. |
| [vectorTo](Point3D_vectorTo.htm) | Returns a vector from this point to another point. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](Point3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Point3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [x](Point3D_x.htm) | Gets and sets the X coordinate of the point. |
| [y](Point3D_y.htm) | Gets and sets the Y coordinate of the point. |
| [z](Point3D_z.htm) | Gets and sets the Z coordinate of the point. |

## Accessed From

[AdditiveFFFLimitsMachineElement.homePosition](AdditiveFFFLimitsMachineElement_homePosition.htm), [AdditiveFFFLimitsMachineElement.parkPosition](AdditiveFFFLimitsMachineElement_parkPosition.htm), [AdditivePlatformMachineElement.origin](AdditivePlatformMachineElement_origin.htm), [AdditivePlatformMachineElement.size](AdditivePlatformMachineElement_size.htm), [AngleValueCommandInput.manipulatorOrigin](AngleValueCommandInput_manipulatorOrigin.htm), [Arc3D.center](Arc3D_center.htm), [Arc3D.endPoint](Arc3D_endPoint.htm), [Arc3D.getData](Arc3D_getData.htm), [Arc3D.startPoint](Arc3D_startPoint.htm), [AreaProperties.centroid](AreaProperties_centroid.htm), [BeamNetwork.vertices](BeamNetwork_vertices.htm), [BoundingBox3D.maxPoint](BoundingBox3D_maxPoint.htm), [BoundingBox3D.minPoint](BoundingBox3D_minPoint.htm), [BRepEdge.pointOnEdge](BRepEdge_pointOnEdge.htm), [BRepFace.centroid](BRepFace_centroid.htm), [BRepFace.pointOnFace](BRepFace_pointOnFace.htm), [BRepVertex.geometry](BRepVertex_geometry.htm), [BRepVertexDefinition.position](BRepVertexDefinition_position.htm), [Camera.eye](Camera_eye.htm), [Camera.target](Camera_target.htm), [Circle3D.center](Circle3D_center.htm), [Circle3D.getData](Circle3D_getData.htm), [Cone.getData](Cone_getData.htm), [Cone.origin](Cone_origin.htm), [ConstructionPoint.geometry](ConstructionPoint_geometry.htm), [CurveEvaluator3D.getEndPoints](CurveEvaluator3D_getEndPoints.htm), [CurveEvaluator3D.getPointAtParameter](CurveEvaluator3D_getPointAtParameter.htm), [CustomGraphicsBillBoard.anchorPoint](CustomGraphicsBillBoard_anchorPoint.htm), [CustomGraphicsCoordinates.getCoordinate](CustomGraphicsCoordinates_getCoordinate.htm), [CustomGraphicsViewPlacement.anchorPoint](CustomGraphicsViewPlacement_anchorPoint.htm), [CustomGraphicsViewScale.anchorPoint](CustomGraphicsViewScale_anchorPoint.htm), [Cylinder.getData](Cylinder_getData.htm), [Cylinder.origin](Cylinder_origin.htm), [DirectionCommandInput.manipulatorOrigin](DirectionCommandInput_manipulatorOrigin.htm), [DistanceValueCommandInput.manipulatorOrigin](DistanceValueCommandInput_manipulatorOrigin.htm), [Ellipse3D.center](Ellipse3D_center.htm), [Ellipse3D.getData](Ellipse3D_getData.htm), [EllipticalArc3D.center](EllipticalArc3D_center.htm), [EllipticalArc3D.getData](EllipticalArc3D_getData.htm), [EllipticalCone.getData](EllipticalCone_getData.htm), [EllipticalCone.origin](EllipticalCone_origin.htm), [EllipticalCylinder.getData](EllipticalCylinder_getData.htm), [EllipticalCylinder.origin](EllipticalCylinder_origin.htm), [FaceGroup.centroid](FaceGroup_centroid.htm), [HoleFeature.position](HoleFeature_position.htm), [InfiniteLine3D.getData](InfiniteLine3D_getData.htm), [InfiniteLine3D.origin](InfiniteLine3D_origin.htm), [JointGeometry.origin](JointGeometry_origin.htm), [Line3D.endPoint](Line3D_endPoint.htm), [Line3D.getData](Line3D_getData.htm), [Line3D.startPoint](Line3D_startPoint.htm), [Matrix3D.getAsCoordinateSystem](Matrix3D_getAsCoordinateSystem.htm), [MeasureResults.positionOne](MeasureResults_positionOne.htm), [MeasureResults.positionThree](MeasureResults_positionThree.htm), [MeasureResults.positionTwo](MeasureResults_positionTwo.htm), [NurbsCurve3D.controlPoints](NurbsCurve3D_controlPoints.htm), [NurbsSurface.controlPoints](NurbsSurface_controlPoints.htm), [OffsetConstraintInput.dimensionPoint](OffsetConstraintInput_dimensionPoint.htm), [OrientedBoundingBox3D.centerPoint](OrientedBoundingBox3D_centerPoint.htm), [PhysicalProperties.centerOfMass](PhysicalProperties_centerOfMass.htm), [Plane.intersectWithLine](Plane_intersectWithLine.htm), [Plane.origin](Plane_origin.htm), [Point3D.copy](Point3D_copy.htm), [Point3D.create](Point3D_create.htm), [PolygonMesh.nodeCoordinates](PolygonMesh_nodeCoordinates.htm), [Polyline3D.points](Polyline3D_points.htm), [RecognizedHole.bottom](RecognizedHole_bottom.htm), [RecognizedHole.top](RecognizedHole_top.htm), [SceneSettings.centerOfFocus](SceneSettings_centerOfFocus.htm), [SceneSettings.groundPosition](SceneSettings_groundPosition.htm), [Selection.point](Selection_point.htm), [Sketch.modelToSketchSpace](Sketch_modelToSketchSpace.htm), [Sketch.origin](Sketch_origin.htm), [Sketch.sketchToModelSpace](Sketch_sketchToModelSpace.htm), [SketchAngularDimension.textPosition](SketchAngularDimension_textPosition.htm), [SketchConcentricCircleDimension.textPosition](SketchConcentricCircleDimension_textPosition.htm), [SketchDiameterDimension.textPosition](SketchDiameterDimension_textPosition.htm), [SketchDimension.textPosition](SketchDimension_textPosition.htm), [SketchDistanceBetweenLineAndPlanarSurfaceDimension.textPosition](SketchDistanceBetweenLineAndPlanarSurfaceDimension_textPosition.htm), [SketchDistanceBetweenPointAndSurfaceDimension.textPosition](SketchDistanceBetweenPointAndSurfaceDimension_textPosition.htm), [SketchEllipseMajorRadiusDimension.textPosition](SketchEllipseMajorRadiusDimension_textPosition.htm), [SketchEllipseMinorRadiusDimension.textPosition](SketchEllipseMinorRadiusDimension_textPosition.htm), [SketchLinearDiameterDimension.textPosition](SketchLinearDiameterDimension_textPosition.htm), [SketchLinearDimension.textPosition](SketchLinearDimension_textPosition.htm), [SketchOffsetCurvesDimension.textPosition](SketchOffsetCurvesDimension_textPosition.htm), [SketchOffsetDimension.textPosition](SketchOffsetDimension_textPosition.htm), [SketchPoint.geometry](SketchPoint_geometry.htm), [SketchPoint.worldGeometry](SketchPoint_worldGeometry.htm), [SketchRadialDimension.textPosition](SketchRadialDimension_textPosition.htm), [SketchTangentDistanceDimension.textPosition](SketchTangentDistanceDimension_textPosition.htm), [SketchText.position](SketchText_position.htm), [SketchTextInput.position](SketchTextInput_position.htm), [Sphere.getData](Sphere_getData.htm), [Sphere.origin](Sphere_origin.htm), [SurfaceEvaluator.getPointAtParameter](SurfaceEvaluator_getPointAtParameter.htm), [Torus.getData](Torus_getData.htm), [Torus.origin](Torus_origin.htm), [TriangleMesh.nodeCoordinates](TriangleMesh_nodeCoordinates.htm), [Vector3D.asPoint](Vector3D_asPoint.htm), [Viewport.viewToModelSpace](Viewport_viewToModelSpace.htm), [VolumetricColorSample.point](VolumetricColorSample_point.htm), [VolumetricSample.point](VolumetricSample_point.htm), [VolumetricScalarSample.point](VolumetricScalarSample_point.htm), [VolumetricVectorSample.point](VolumetricVectorSample_point.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [SketchArcs.addByCenterStartSweep](SketchArcs_addByCenterStartaSweep_Sample.htm) | Demonstrates the SketchArcs.addByCenterStartSweep method. |
| [SketchArcs.addByThreePoints](SketchArcs_addByThreePoints_Sample.htm) | Demonstrates the SketchArcs.addByThreePoints method. |
| [SketchArcs.addFillet](SketchArcs_addFillet_Sample.htm) | Demonstrates the SketchArcs.addFillet method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |