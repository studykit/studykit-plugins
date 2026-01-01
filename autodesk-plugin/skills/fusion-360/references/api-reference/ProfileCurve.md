# ProfileCurve Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Sketch/ProfileCurve.h>

## Description

A single curve in a profile.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ProfileCurve_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](ProfileCurve_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. Returns null if this isn't the NativeObject. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](ProfileCurve_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [boundingBox](ProfileCurve_boundingBox.htm) | Returns the bounding box of the profile curve in sketch space. |
| [geometry](ProfileCurve_geometry.htm) | Returns the geometric entity of this portion of the profile. |
| [geometryType](ProfileCurve_geometryType.htm) | Return the geometry type that the Geometry property will return. |
| [isValid](ProfileCurve_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](ProfileCurve_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](ProfileCurve_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [parentProfile](ProfileCurve_parentProfile.htm) | Returns the parent Profile object. |
| [parentProfileLoop](ProfileCurve_parentProfileLoop.htm) | Returns the parent ProfileLoop object. |
| [parentSketch](ProfileCurve_parentSketch.htm) | Returns the parent Profile object. |
| [sketchEntity](ProfileCurve_sketchEntity.htm) | Returns the associated sketch entity that defines this curve. |

## Accessed From

[ProfileCurve.createForAssemblyContext](ProfileCurve_createForAssemblyContext.htm), [ProfileCurve.nativeObject](ProfileCurve_nativeObject.htm), [ProfileCurves.item](ProfileCurves_item.htm)

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |