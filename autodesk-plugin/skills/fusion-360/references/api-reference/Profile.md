# Profile Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/Profile.h>

## Description

Represents a profile in a sketch. Profiles are automatically computed by Fusion and represent closed areas within the sketch.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [areaProperties](Profile_areaProperties.htm) | Calculates the area properties for the profile. |
| [classType](Profile_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](Profile_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. Returns null if this isn't the NativeObject. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](Profile_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [boundingBox](Profile_boundingBox.htm) | Returns the 3D bounding box of the profile in sketch space. |
| [entityToken](Profile_entityToken.htm) | Returns a token for the Profile object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same profile. |
| [face](Profile_face.htm) | Returns a temporary BRepFace object that is the same shape as the profile. The geometry of the returned face is defined in the 3D space of the parent sketch of the profile.   This can be useful when wanting to use a profile in conjunction with the TemporaryBRepManager object to create B-Rep objects. |
| [isValid](Profile_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](Profile_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](Profile_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentSketch](Profile_parentSketch.htm) | Returns the parent sketch of the profile. |
| [plane](Profile_plane.htm) | Returns the plane the profile is defined in. Profiles are always planar and exist within a single plane. |
| [profileLoops](Profile_profileLoops.htm) | The loops or closed areas within this profile. There is always a single outer loop but there can be zero to many inner loops defining voids in the profile. |

## Accessed From

[Component.createBRepEdgeProfile](Component_createBRepEdgeProfile.htm), [Component.createOpenProfile](Component_createOpenProfile.htm), [FlatPatternComponent.createBRepEdgeProfile](FlatPatternComponent_createBRepEdgeProfile.htm), [FlatPatternComponent.createOpenProfile](FlatPatternComponent_createOpenProfile.htm), [Profile.createForAssemblyContext](Profile_createForAssemblyContext.htm), [Profile.nativeObject](Profile_nativeObject.htm), [ProfileCurve.parentProfile](ProfileCurve_parentProfile.htm), [ProfileLoop.parentProfile](ProfileLoop_parentProfile.htm), [Profiles.item](Profiles_item.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |