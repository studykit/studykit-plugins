# Matrix3D Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::core" and the header file is <Core/Geometry/Matrix3D.h>

## Description

Transient 3D 4x4 matrix. This object is a wrapper over 3D matrix data and is used as way to pass matrix data in and out of the API and as a convenience when operating on matrix data. They are created statically using the create method of the Matrix3D class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [asArray](Matrix3D_asArray.htm) | Returns the contents of the matrix as a 16 element array. |
| [classType](Matrix3D_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [copy](Matrix3D_copy.htm) | Creates an independent copy of this matrix. |
| [create](Matrix3D_create.htm) | Creates a transient 3d matrix object. It is initialized as an identity matrix and is created statically using the Matrix3D.create method. |
| [getAsCoordinateSystem](Matrix3D_getAsCoordinateSystem.htm) | Gets the matrix data as the components that define a coordinate system. |
| [getCell](Matrix3D_getCell.htm) | Gets the value of the specified cell in the 4x4 matrix. |
| [invert](Matrix3D_invert.htm) | Inverts this matrix. |
| [isEqualTo](Matrix3D_isEqualTo.htm) | Compares this matrix with another matrix and returns True if they're identical. |
| [setCell](Matrix3D_setCell.htm) | Sets the specified cell in the 4x4 matrix to the specified value. |
| [setToAlignCoordinateSystems](Matrix3D_setToAlignCoordinateSystems.htm) | Sets this matrix to be the matrix that maps from the 'from' coordinate system to the 'to' coordinate system. |
| [setToIdentity](Matrix3D_setToIdentity.htm) | Resets this matrix to an identify matrix. |
| [setToRotateTo](Matrix3D_setToRotateTo.htm) | Sets to the matrix of rotation that would align the 'from' vector with the 'to' vector. The optional axis argument may be used when the two vectors are perpendicular and in opposite directions to specify a specific solution, but is otherwise ignored |
| [setToRotation](Matrix3D_setToRotation.htm) | Sets this matrix to the matrix of rotation by the specified angle, through the specified origin, around the specified axis |
| [setWithArray](Matrix3D_setWithArray.htm) | Sets the contents of the array using a 16 element array. |
| [setWithCoordinateSystem](Matrix3D_setWithCoordinateSystem.htm) | Sets the matrix based on the components of a coordinate system. |
| [transformBy](Matrix3D_transformBy.htm) | Transforms this matrix using the input matrix. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [determinant](Matrix3D_determinant.htm) | Returns the determinant of the matrix. |
| [isValid](Matrix3D_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](Matrix3D_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [translation](Matrix3D_translation.htm) | Gets and sets the translation component of the matrix. |

## Accessed From

[AsBuiltJoint.transform](AsBuiltJoint_transform.htm), [ConstructionPlane.transform](ConstructionPlane_transform.htm), [CustomGraphicsBRepBody.transform](CustomGraphicsBRepBody_transform.htm), [CustomGraphicsCurve.transform](CustomGraphicsCurve_transform.htm), [CustomGraphicsEntity.transform](CustomGraphicsEntity_transform.htm), [CustomGraphicsGroup.transform](CustomGraphicsGroup_transform.htm), [CustomGraphicsLines.transform](CustomGraphicsLines_transform.htm), [CustomGraphicsMesh.transform](CustomGraphicsMesh_transform.htm), [CustomGraphicsPointSet.transform](CustomGraphicsPointSet_transform.htm), [CustomGraphicsText.transform](CustomGraphicsText_transform.htm), [Decal.transform](Decal_transform.htm), [DecalInput.transform](DecalInput_transform.htm), [Joint.geometryOneTransform](Joint_geometryOneTransform.htm), [Joint.geometryTwoTransform](Joint_geometryTwoTransform.htm), [JointOrigin.transform](JointOrigin_transform.htm), [Matrix3D.copy](Matrix3D_copy.htm), [Matrix3D.create](Matrix3D_create.htm), [Matrix3DGraphNodeProperty.value](Matrix3DGraphNodeProperty_value.htm), [MoveFeature.transform](MoveFeature_transform.htm), [MoveFeatureFreeMoveDefinition.transform](MoveFeatureFreeMoveDefinition_transform.htm), [MoveFeatureInput.transform](MoveFeatureInput_transform.htm), [Occurrence.initialTransform](Occurrence_initialTransform.htm), [Occurrence.transform](Occurrence_transform.htm), [Occurrence.transform2](Occurrence_transform2.htm), [OptimizedOrientationResult.transformation](OptimizedOrientationResult_transformation.htm), [PatternElement.transform](PatternElement_transform.htm), [ProjectedTextureMapControl.transform](ProjectedTextureMapControl_transform.htm), [SectionAnalysis.initialPosition](SectionAnalysis_initialPosition.htm), [SectionAnalysis.transform](SectionAnalysis_transform.htm), [SectionAnalysisInput.initialPosition](SectionAnalysisInput_initialPosition.htm), [SectionAnalysisInput.transform](SectionAnalysisInput_transform.htm), [Setup.workCoordinateSystem](Setup_workCoordinateSystem.htm), [Sketch.transform](Sketch_transform.htm), [SVGImportOptions.transform](SVGImportOptions_transform.htm), [TextureMapControl3D.transform](TextureMapControl3D_transform.htm), [TriadCommandInput.lastTransform](TriadCommandInput_lastTransform.htm), [TriadCommandInput.positionTransform](TriadCommandInput_positionTransform.htm), [TriadCommandInput.transform](TriadCommandInput_transform.htm), [Viewport.modelToViewSpaceTransform](Viewport_modelToViewSpaceTransform.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [moveFeatures.add](moveFeatures_add_Sample.htm) | Demonstrates the moveFeatures.add method. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |