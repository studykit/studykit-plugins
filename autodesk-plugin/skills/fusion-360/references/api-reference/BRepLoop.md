# BRepLoop Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/BRep/BRepLoop.h>

## Description

Represents a connected portion of a BRepFace boundary. It consists of a chain of BRepCoEdges.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BRepLoop_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](BRepLoop_createForAssemblyContext.htm) | Returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](BRepLoop_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this BRepLoop object is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly. but is already the native object. |
| [body](BRepLoop_body.htm) | Returns the parent body of the loop. |
| [boundingBox](BRepLoop_boundingBox.htm) | Returns the bounding box of this loop |
| [coEdges](BRepLoop_coEdges.htm) | Returns the BRepCoEdges consisting this loop |
| [edges](BRepLoop_edges.htm) | Returns the BRepEdges used by this loop |
| [entityToken](BRepLoop_entityToken.htm) | Returns a token for the BRepLoop object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same loop. |
| [face](BRepLoop_face.htm) | Returns the parent face of the loop. |
| [isOuter](BRepLoop_isOuter.htm) | Returns true of this loop is an outer loop of a face |
| [isValid](BRepLoop_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](BRepLoop_nativeObject.htm) | The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](BRepLoop_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[BRepCoEdge.loop](BRepCoEdge_loop.htm), [BRepLoop.createForAssemblyContext](BRepLoop_createForAssemblyContext.htm), [BRepLoop.nativeObject](BRepLoop_nativeObject.htm), [BRepLoops.item](BRepLoops_item.htm), [UntrimFeature.loopsToUntrim](UntrimFeature_loopsToUntrim.htm), [UntrimFeatureInput.loopsToUntrim](UntrimFeatureInput_loopsToUntrim.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Patch Feature API Sample](PatchFeatureSample_Sample.htm) | Demonstrates creating a new patch feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |