# ConstructionAxis Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionAxis.h>

## Description

ConstructionAxis Object

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionAxis_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](ConstructionAxis_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](ConstructionAxis_deleteMe.htm) | Deletes the construction axis. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](ConstructionAxis_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](ConstructionAxis_attributes.htm) | Returns the collection of attributes associated with this construction axis. |
| [baseFeature](ConstructionAxis_baseFeature.htm) | If this construction axis is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [component](ConstructionAxis_component.htm) | Returns the component this construction plane belongs to. |
| [definition](ConstructionAxis_definition.htm) | Returns the construction axis definition object which provides access to the information defining the construction axis. |
| [entityToken](ConstructionAxis_entityToken.htm) | Returns a token for the ConstructionAxis object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same construction axis. |
| [errorOrWarningMessage](ConstructionAxis_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [geometry](ConstructionAxis_geometry.htm) | Returns an infinite line that represents the position and orientation of the construction axis. This geometry is defined in the AssemblyContext of this ConstructionAxis. |
| [healthState](ConstructionAxis_healthState.htm) | Returns the current health state of this construction axis. |
| [isDeletable](ConstructionAxis_isDeletable.htm) | Indicates if this construction axis can be deleted. Base construction axes can not be deleted. |
| [isLightBulbOn](ConstructionAxis_isLightBulbOn.htm) | Indicates if the light bulb (as displayed in the browser) is on. A construction axis will only be visible if it's light bulb, and that of it's containing folder and parent component/s are also on. |
| [isParametric](ConstructionAxis_isParametric.htm) | Indicates if this construction axis is parametric or not. |
| [isValid](ConstructionAxis_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](ConstructionAxis_isVisible.htm) | Gets if the construction plane is visible. This property is affected by the AssemblyContext of the construction axis. |
| [name](ConstructionAxis_name.htm) | The name of the construction axis as it is shown in the browser. |
| [nativeObject](ConstructionAxis_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of it's parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](ConstructionAxis_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parent](ConstructionAxis_parent.htm) | Returns the parent component or base feature. If both the design and the construction axis are parametric, the parent will be a component. If the design is parametric and the construction axis is not, the parent will be a base feature. If the design is not parametric the parent will be a component. |
| [timelineObject](ConstructionAxis_timelineObject.htm) | Returns the timeline object associated with this construction axis. |

## Accessed From

[BaseFeature.constructionAxes](BaseFeature_constructionAxes.htm), [Component.xConstructionAxis](Component_xConstructionAxis.htm), [Component.yConstructionAxis](Component_yConstructionAxis.htm), [Component.zConstructionAxis](Component_zConstructionAxis.htm), [ConstructionAxes.add](ConstructionAxes_add.htm), [ConstructionAxes.item](ConstructionAxes_item.htm), [ConstructionAxes.itemByName](ConstructionAxes_itemByName.htm), [ConstructionAxis.createForAssemblyContext](ConstructionAxis_createForAssemblyContext.htm), [ConstructionAxis.nativeObject](ConstructionAxis_nativeObject.htm), [ConstructionAxisByLineDefinition.parentConstructionAxis](ConstructionAxisByLineDefinition_parentConstructionAxis.htm), [ConstructionAxisCircularFaceDefinition.parentConstructionAxis](ConstructionAxisCircularFaceDefinition_parentConstructionAxis.htm), [ConstructionAxisDefinition.parentConstructionAxis](ConstructionAxisDefinition_parentConstructionAxis.htm), [ConstructionAxisEdgeDefinition.parentConstructionAxis](ConstructionAxisEdgeDefinition_parentConstructionAxis.htm), [ConstructionAxisNormalToFaceAtPointDefinition.parentConstructionAxis](ConstructionAxisNormalToFaceAtPointDefinition_parentConstructionAxis.htm), [ConstructionAxisPerpendicularAtPointDefinition.parentConstructionAxis](ConstructionAxisPerpendicularAtPointDefinition_parentConstructionAxis.htm), [ConstructionAxisTwoPlaneDefinition.parentConstructionAxis](ConstructionAxisTwoPlaneDefinition_parentConstructionAxis.htm), [ConstructionAxisTwoPointDefinition.parentConstructionAxis](ConstructionAxisTwoPointDefinition_parentConstructionAxis.htm), [FlatPatternComponent.xConstructionAxis](FlatPatternComponent_xConstructionAxis.htm), [FlatPatternComponent.yConstructionAxis](FlatPatternComponent_yConstructionAxis.htm), [FlatPatternComponent.zConstructionAxis](FlatPatternComponent_zConstructionAxis.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Axis API Sample](ConstructionAxisSample_Sample.htm) | Demonstrates creating construction axis in various ways. |
| [Create Setups From Hole Recognition API Sample](CreateSetupsFromHoleRecognition_Sample.htm) | This sample script demonstrates how to create a correctly oriented setup using Hole Recognition functionality.  The Fusion Manufacturing Extension is required for Hole Recognition.  The script starts by opening a sample model from the CAM Samples folder via its URN. The model comprises a 3 way coupling containing holes in various orientations and mounted on a fixture. A reference setup is created for the model using a simple stock mode and offsets. The Hole Recognition feature of the Fusion Manufacturing Extension creates 5 hole groups containing 11 holes between them. For each unique hole group vector captured, a new setup is created and its orientation transformed to match the vector. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |