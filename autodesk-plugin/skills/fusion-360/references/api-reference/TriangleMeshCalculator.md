# TriangleMeshCalculator Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshData/TriangleMeshCalculator.h>

## Description

Used to calculate new meshes for a B-Rep or T-Spline using defined criteria.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [calculate](TriangleMeshCalculator_calculate.htm) | Calculates a new triangle mesh based on the current settings. |
| [classType](TriangleMeshCalculator_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [setQuality](TriangleMeshCalculator_setQuality.htm) | This is a simplified way to set the various settings that control the resulting mesh. When used it automatically adjusts all of the property values appropriately. It does this for the given geometry by computing its bounding box diameter. Then the surface tolerance is calculated as shown below where the meshLOD is the "Level of Detail" and is described in more detail below. The diameter is the bounding box diameter. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [isValid](TriangleMeshCalculator_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [maxAspectRatio](TriangleMeshCalculator_maxAspectRatio.htm) | Specifies the maximum length to height ratio that a triangle can have. This helps to avoid long skinny triangles. A value of 0 (the default) indicates that no maximum aspect ratio is specified. |
| [maxNormalDeviation](TriangleMeshCalculator_maxNormalDeviation.htm) | Specifies the maximum deviation between adjacent vertex normals. This value is the maximum angle allowed between normals and is specified in radians. A value of 0 (the default) indicates that no normal deviation is specified. |
| [maxSideLength](TriangleMeshCalculator_maxSideLength.htm) | Specifies the maximum side of any triangle in the mesh. A value of 0 (the default) indicates that no maximum length is specified. The value is specified in centimeters. |
| [objectType](TriangleMeshCalculator_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentMeshManager](TriangleMeshCalculator_parentMeshManager.htm) | Returns the parent MeshManager object. |
| [surfaceTolerance](TriangleMeshCalculator_surfaceTolerance.htm) | Specifies the maximum distance that the mesh can deviate from the smooth surface. The value is in centimeters. Smaller values can result in a much greater number of facets being returned and will require more processing time to calculate. |

## Accessed From

[MeshManager.createMeshCalculator](MeshManager_createMeshCalculator.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |