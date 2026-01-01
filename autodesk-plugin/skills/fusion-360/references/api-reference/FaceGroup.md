# FaceGroup Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/MeshBody/FaceGroup.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

Represent a connected region on a single geometric surface.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](FaceGroup_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](FaceGroup_createForAssemblyContext.htm) | Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [area](FaceGroup_area.htm) | Returns the area in cm ^ 2. |
| [assemblyContext](FaceGroup_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this face group object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [boundingBox](FaceGroup_boundingBox.htm) | Returns the bounding box of this face |
| [centroid](FaceGroup_centroid.htm) | Returns a point at the centroid (aka, geometric center) of the face. |
| [entityToken](FaceGroup_entityToken.htm) | Returns a token for the face group object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same face. |
| [isPlanar](FaceGroup_isPlanar.htm) | Returns if the face group is planar or not. |
| [isValid](FaceGroup_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](FaceGroup_nativeObject.htm) | The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](FaceGroup_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentBody](FaceGroup_parentBody.htm) | Returns the parent body of the face. |
| [tempId](FaceGroup_tempId.htm) | Returns the temporary ID of this face group. This ID is only good while the document remains open and as long as the owning mesh body is not modified in any way. |

## Accessed From

[FaceGroup.createForAssemblyContext](FaceGroup_createForAssemblyContext.htm), [FaceGroup.nativeObject](FaceGroup_nativeObject.htm), [FaceGroups.item](FaceGroups_item.htm), [MeshCombineFaceGroupsFeature.inputFaceGroups](MeshCombineFaceGroupsFeature_inputFaceGroups.htm), [MeshCombineFaceGroupsFeatureInput.inputFaceGroups](MeshCombineFaceGroupsFeatureInput_inputFaceGroups.htm)

## Version

Introduced in version September 2024

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |