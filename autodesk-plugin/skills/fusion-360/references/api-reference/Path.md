# Path Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/Path.h>

## Description

The Path object represents a single set of connected curves. The order of the objects within the collection is the same as the connection order of the entities. When using a Path to create a feature, the Path serves as a way to pass in the set of sketch entities and edges. When getting the Path of an existing feature it returns the actual path used to define the feature geometry. In cases like a sweep feature, this can result in using portions of the original input sketch curves or edges and the returned path will provide these "partial" curves as the PathEntity objects.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [addCurves](Path_addCurves.htm) | Adds additional curves to the existing path. This can be useful when creating a complex path for a sweep and you want to include sets of curves from multiple sketches and edges from multiple bodies. |
| [classType](Path_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [create](Path_create.htm) | Creates a new Path that can be used as input to various features. For example, it is used to create an open set of curves to create surfaces using extrude, revolve, and sweep. It is also used to create the path for a sweep and sections and profiles and rails for lofts. And it is used to define the boundary of a patch feature. |
| [createForAssemblyContext](Path_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [item](Path_item.htm) | Function that returns the specified PathEntity using an index into the collection. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](Path_assemblyContext.htm) | This property is not supported for the Path object. |
| [count](Path_count.htm) | The number of curves in the path. |
| [isClosed](Path_isClosed.htm) | Indicates if the path is closed or not. Returns True in the case of a closed path. |
| [isValid](Path_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [nativeObject](Path_nativeObject.htm) | This property is not supported for the Path object. |
| [objectType](Path_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |

## Accessed From

[Features.createPath](Features_createPath.htm), [Path.create](Path_create.htm), [Path.createForAssemblyContext](Path_createForAssemblyContext.htm), [Path.nativeObject](Path_nativeObject.htm), [PathEntity.parentPath](PathEntity_parentPath.htm), [PathPatternFeature.path](PathPatternFeature_path.htm), [PathPatternFeatureInput.path](PathPatternFeatureInput_path.htm), [PipeFeature.path](PipeFeature_path.htm), [PipeFeatureInput.path](PipeFeatureInput_path.htm), [SweepFeature.guideRail](SweepFeature_guideRail.htm), [SweepFeature.path](SweepFeature_path.htm), [SweepFeatureInput.guideRail](SweepFeatureInput_guideRail.htm), [SweepFeatureInput.path](SweepFeatureInput_path.htm)

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |