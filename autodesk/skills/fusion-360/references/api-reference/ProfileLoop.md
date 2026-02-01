# ProfileLoop Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileLoop.h>

## Description

A loop within a profile.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ProfileLoop_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](ProfileLoop_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. Returns null if this isn't the NativeObject. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](ProfileLoop_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [isOuter](ProfileLoop_isOuter.htm) | Indicates if this is an outer or inner loop. Profiles always have one outer loop and have an zero to many inner loops defining voids. |
| [isValid](ProfileLoop_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](ProfileLoop_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](ProfileLoop_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentProfile](ProfileLoop_parentProfile.htm) | Returns the parent Profile object. |
| [profileCurves](ProfileLoop_profileCurves.htm) | Returns a collection of the curves making up this loop. |

## Accessed From

[ProfileCurve.parentProfileLoop](ProfileCurve_parentProfileLoop.htm), [ProfileLoop.createForAssemblyContext](ProfileLoop_createForAssemblyContext.htm), [ProfileLoop.nativeObject](ProfileLoop_nativeObject.htm), [ProfileLoops.item](ProfileLoops_item.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |