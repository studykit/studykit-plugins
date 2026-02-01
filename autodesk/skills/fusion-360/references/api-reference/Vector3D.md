# Vector3D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Vector3D.h>

## Description

Transient 3D vector. This object is a wrapper over 3D vector data and is used as way to pass vector data in and out of the API and as a convenience when operating on vector data. They are created statically using the create method of the Vector3D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [add](Vector3D_add.htm) | Adds a vector to this vector. |
| [angleTo](Vector3D_angleTo.htm) | Determines the angle between this vector and the specified vector. |
| [asArray](Vector3D_asArray.htm) | Returns the vector coordinates as an array [x, y, z]. |
| [asPoint](Vector3D_asPoint.htm) | Returns a new point with the same coordinate values as this vector. |
| [classType](Vector3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Vector3D_copy.htm) | Creates a copy of this vector. |
| [create](Vector3D_create.htm) | Creates a 3D vector object. This object is created statically using the Vector3D.create method. |
| [crossProduct](Vector3D_crossProduct.htm) | Returns the cross product between this vector and the specified vector. |
| [dotProduct](Vector3D_dotProduct.htm) | Returns the dot product between this vector and the specified vector. |
| [isEqualTo](Vector3D_isEqualTo.htm) | Determines if this vector is equal to the specified vector. |
| [isParallelTo](Vector3D_isParallelTo.htm) | Determines if the input vector is parallel with this vector. |
| [isPerpendicularTo](Vector3D_isPerpendicularTo.htm) | Determines if the input vector is perpendicular to this vector. |
| [normalize](Vector3D_normalize.htm) | Makes this vector of unit length. This vector should not be zero length. |
| [scaleBy](Vector3D_scaleBy.htm) | Scale this vector by the specified product. |
| [setWithArray](Vector3D_setWithArray.htm) | Reset this vector with the coordinate values in an array [x, y, z]. |
| [subtract](Vector3D_subtract.htm) | Subtract a vector from this vector. |
| [transformBy](Vector3D_transformBy.htm) | Transform this vector by the specified matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](Vector3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [length](Vector3D_length.htm) | Get the length of this vector. |
| [objectType](Vector3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [x](Vector3D_x.htm) | The x value. |
| [y](Vector3D_y.htm) | The y value. |
| [z](Vector3D_z.htm) | The z value. |

## Accessed From

[AngleValueCommandInput.manipulatorXDirection](AngleValueCommandInput_manipulatorXDirection.htm), [AngleValueCommandInput.manipulatorYDirection](AngleValueCommandInput_manipulatorYDirection.htm), [Arc3D.getData](Arc3D_getData.htm), [Arc3D.normal](Arc3D_normal.htm), [Arc3D.referenceVector](Arc3D_referenceVector.htm), [AreaProperties.getPrincipalAxes](AreaProperties_getPrincipalAxes.htm), [ArrangeComponent.upDirection](ArrangeComponent_upDirection.htm), [ArrangeComponent.zeroDirection](ArrangeComponent_zeroDirection.htm), [BallJointMotion.pitchDirectionVector](BallJointMotion_pitchDirectionVector.htm), [BallJointMotion.rollDirectionVector](BallJointMotion_rollDirectionVector.htm), [BallJointMotion.yawDirectionVector](BallJointMotion_yawDirectionVector.htm), [BossFeature.direction](BossFeature_direction.htm), [Camera.upVector](Camera_upVector.htm), [Circle3D.getData](Circle3D_getData.htm), [Circle3D.normal](Circle3D_normal.htm), [Cone.axis](Cone_axis.htm), [Cone.getData](Cone_getData.htm), [CurveEvaluator3D.getCurvature](CurveEvaluator3D_getCurvature.htm), [CurveEvaluator3D.getFirstDerivative](CurveEvaluator3D_getFirstDerivative.htm), [CurveEvaluator3D.getSecondDerivative](CurveEvaluator3D_getSecondDerivative.htm), [CurveEvaluator3D.getTangent](CurveEvaluator3D_getTangent.htm), [CurveEvaluator3D.getThirdDerivative](CurveEvaluator3D_getThirdDerivative.htm), [CustomGraphicsBillBoard.axis](CustomGraphicsBillBoard_axis.htm), [Cylinder.axis](Cylinder_axis.htm), [Cylinder.getData](Cylinder_getData.htm), [CylindricalJointMotion.rotationAxisVector](CylindricalJointMotion_rotationAxisVector.htm), [DirectionCommandInput.manipulatorDirection](DirectionCommandInput_manipulatorDirection.htm), [DistanceValueCommandInput.manipulatorDirection](DistanceValueCommandInput_manipulatorDirection.htm), [Ellipse3D.getData](Ellipse3D_getData.htm), [Ellipse3D.majorAxis](Ellipse3D_majorAxis.htm), [Ellipse3D.normal](Ellipse3D_normal.htm), [EllipticalArc3D.getData](EllipticalArc3D_getData.htm), [EllipticalArc3D.majorAxis](EllipticalArc3D_majorAxis.htm), [EllipticalArc3D.normal](EllipticalArc3D_normal.htm), [EllipticalCone.getAxes](EllipticalCone_getAxes.htm), [EllipticalCone.getData](EllipticalCone_getData.htm), [EllipticalCylinder.axis](EllipticalCylinder_axis.htm), [EllipticalCylinder.getData](EllipticalCylinder_getData.htm), [EllipticalCylinder.majorAxis](EllipticalCylinder_majorAxis.htm), [HoleFeature.direction](HoleFeature_direction.htm), [InfiniteLine3D.direction](InfiniteLine3D_direction.htm), [InfiniteLine3D.getData](InfiniteLine3D_getData.htm), [JointGeometry.primaryAxisVector](JointGeometry_primaryAxisVector.htm), [JointGeometry.secondaryAxisVector](JointGeometry_secondaryAxisVector.htm), [JointGeometry.thirdAxisVector](JointGeometry_thirdAxisVector.htm), [JointOrigin.primaryAxisVector](JointOrigin_primaryAxisVector.htm), [JointOrigin.secondaryAxisVector](JointOrigin_secondaryAxisVector.htm), [JointOrigin.thirdAxisVector](JointOrigin_thirdAxisVector.htm), [JointOriginInput.primaryAxisVector](JointOriginInput_primaryAxisVector.htm), [JointOriginInput.secondaryAxisVector](JointOriginInput_secondaryAxisVector.htm), [JointOriginInput.thirdAxisVector](JointOriginInput_thirdAxisVector.htm), [LinearMachineAxis.direction](LinearMachineAxis_direction.htm), [LinearMachineAxisInput.direction](LinearMachineAxisInput_direction.htm), [Matrix3D.getAsCoordinateSystem](Matrix3D_getAsCoordinateSystem.htm), [Matrix3D.translation](Matrix3D_translation.htm), [MultiAxisRetractAndReconfigureSettings.stockExpansion](MultiAxisRetractAndReconfigureSettings_stockExpansion.htm), [OrientedBoundingBox3D.heightDirection](OrientedBoundingBox3D_heightDirection.htm), [OrientedBoundingBox3D.lengthDirection](OrientedBoundingBox3D_lengthDirection.htm), [OrientedBoundingBox3D.widthDirection](OrientedBoundingBox3D_widthDirection.htm), [PhysicalProperties.getPrincipalAxes](PhysicalProperties_getPrincipalAxes.htm), [PinSlotJointMotion.rotationAxisVector](PinSlotJointMotion_rotationAxisVector.htm), [PinSlotJointMotion.slideDirectionVector](PinSlotJointMotion_slideDirectionVector.htm), [PlanarJointMotion.normalDirectionVector](PlanarJointMotion_normalDirectionVector.htm), [PlanarJointMotion.primarySlideDirectionVector](PlanarJointMotion_primarySlideDirectionVector.htm), [PlanarJointMotion.secondarySlideDirectionVector](PlanarJointMotion_secondarySlideDirectionVector.htm), [Plane.normal](Plane_normal.htm), [Plane.uDirection](Plane_uDirection.htm), [Plane.vDirection](Plane_vDirection.htm), [Point3D.asVector](Point3D_asVector.htm), [Point3D.vectorTo](Point3D_vectorTo.htm), [PolygonMesh.normalVectors](PolygonMesh_normalVectors.htm), [RecognizedHole.axis](RecognizedHole_axis.htm), [RecognizedHoleSegment.axis](RecognizedHoleSegment_axis.htm), [RectangularPatternFeature.directionOne](RectangularPatternFeature_directionOne.htm), [RectangularPatternFeature.directionTwo](RectangularPatternFeature_directionTwo.htm), [RectangularPatternFeatureInput.directionOne](RectangularPatternFeatureInput_directionOne.htm), [RectangularPatternFeatureInput.directionTwo](RectangularPatternFeatureInput_directionTwo.htm), [RevoluteJointMotion.rotationAxisVector](RevoluteJointMotion_rotationAxisVector.htm), [Sketch.xDirection](Sketch_xDirection.htm), [Sketch.yDirection](Sketch_yDirection.htm), [SketchEllipse.majorAxis](SketchEllipse_majorAxis.htm), [SketchEllipticalArc.majorAxis](SketchEllipticalArc_majorAxis.htm), [SliderJointMotion.slideDirectionVector](SliderJointMotion_slideDirectionVector.htm), [SurfaceEvaluator.getCurvature](SurfaceEvaluator_getCurvature.htm), [SurfaceEvaluator.getFirstDerivative](SurfaceEvaluator_getFirstDerivative.htm), [SurfaceEvaluator.getNormalAtParameter](SurfaceEvaluator_getNormalAtParameter.htm), [SurfaceEvaluator.getNormalAtPoint](SurfaceEvaluator_getNormalAtPoint.htm), [SurfaceEvaluator.getSecondDerivative](SurfaceEvaluator_getSecondDerivative.htm), [SurfaceEvaluator.getThirdDerivative](SurfaceEvaluator_getThirdDerivative.htm), [ToEntityExtentDefinition.directionHint](ToEntityExtentDefinition_directionHint.htm), [Torus.axis](Torus_axis.htm), [Torus.getData](Torus_getData.htm), [TriangleMesh.normalVectors](TriangleMesh_normalVectors.htm), [Vector3D.copy](Vector3D_copy.htm), [Vector3D.create](Vector3D_create.htm), [Vector3D.crossProduct](Vector3D_crossProduct.htm), [Vector3DGraphNodeProperty.value](Vector3DGraphNodeProperty_value.htm), [Viewport.frontEyeDirection](Viewport_frontEyeDirection.htm), [Viewport.frontUpDirection](Viewport_frontUpDirection.htm), [VolumetricVectorSample.value](VolumetricVectorSample_value.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |
| [moveFeatures.add](moveFeatures_add_Sample.htm) | Demonstrates the moveFeatures.add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |