# ConstructionPlane Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Construction/ConstructionPlane.h>

## Description

ConstructionPlane Object

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ConstructionPlane_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](ConstructionPlane_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](ConstructionPlane_deleteMe.htm) | Deletes the construction plane. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](ConstructionPlane_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](ConstructionPlane_attributes.htm) | Returns the collection of attributes associated with this construction plane. |
| [baseFeature](ConstructionPlane_baseFeature.htm) | If this construction plane is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [component](ConstructionPlane_component.htm) | Returns the component this construction plane belongs to. |
| [definition](ConstructionPlane_definition.htm) | Returns the ConstructionPlaneDefinition object which provides access to the information defining this ConstructionPlane. |
| [displayBounds](ConstructionPlane_displayBounds.htm) | Gets and sets the display size of the construction plane. The bounding box defines the min and max corners of the plane as defined in the 2D space of the construction plane. |
| [entityToken](ConstructionPlane_entityToken.htm) | Returns a token for the ConstructionPlane object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same construction plane. |
| [errorOrWarningMessage](ConstructionPlane_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [geometry](ConstructionPlane_geometry.htm) | Returns a plane that represents the position and orientation of the construction plane. This geometry is defined in the AssemblyContext of this ConstructionPlane. |
| [healthState](ConstructionPlane_healthState.htm) | Returns the current health state of this construction plane. |
| [isDeletable](ConstructionPlane_isDeletable.htm) | Indicates if this construction plane can be deleted. Base construction planes can not be deleted. |
| [isLightBulbOn](ConstructionPlane_isLightBulbOn.htm) | Indicates if the light bulb (as displayed in the browser) is on. A construction plane will only be visible if it's light bulb, and that of it's containing folder and parent component/s are also on. |
| [isParametric](ConstructionPlane_isParametric.htm) | Indicates if this construction plane is parametric or not. |
| [isValid](ConstructionPlane_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVisible](ConstructionPlane_isVisible.htm) | Indicates if the construction plane is visible. This property is affected by the AssemblyContext of the construction plane. |
| [name](ConstructionPlane_name.htm) | Returns the name of the construction plane as it is shown in the browser. |
| [nativeObject](ConstructionPlane_nativeObject.htm) | The NativeObject is the object outside the context of an assembly. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](ConstructionPlane_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parent](ConstructionPlane_parent.htm) | Returns the parent component or base feature. If both the design and the construction plane are parametric, the parent will be a component. If the design is parametric and the construction plane is not, the parent will be a base feature. If the design is not parametric the parent will be a component. |
| [timelineObject](ConstructionPlane_timelineObject.htm) | Returns the timeline object associated with this construction plane. |
| [transform](ConstructionPlane_transform.htm) | Returns the current position and orientation of the construction plane as a matrix. For a parametric construction plane, this property is read-only. For a construction plane in a direct modeling model or in a base feature, this is read-write and can be used to reposition the constructions plane. |

## Accessed From

[Arrange2DPlaneEnvelopeInput.plane](Arrange2DPlaneEnvelopeInput_plane.htm), [Arrange3DEnvelopeDefinition.plane](Arrange3DEnvelopeDefinition_plane.htm), [Arrange3DEnvelopeInput.plane](Arrange3DEnvelopeInput_plane.htm), [ArrangePlaneEnvelopeDefinition.plane](ArrangePlaneEnvelopeDefinition_plane.htm), [BaseFeature.constructionPlanes](BaseFeature_constructionPlanes.htm), [Component.xYConstructionPlane](Component_xYConstructionPlane.htm), [Component.xZConstructionPlane](Component_xZConstructionPlane.htm), [Component.yZConstructionPlane](Component_yZConstructionPlane.htm), [ConstructionPlane.createForAssemblyContext](ConstructionPlane_createForAssemblyContext.htm), [ConstructionPlane.nativeObject](ConstructionPlane_nativeObject.htm), [ConstructionPlaneAtAngleDefinition.parentConstructionPlane](ConstructionPlaneAtAngleDefinition_parentConstructionPlane.htm), [ConstructionPlaneByPlaneDefinition.parentConstructionPlane](ConstructionPlaneByPlaneDefinition_parentConstructionPlane.htm), [ConstructionPlaneDefinition.parentConstructionPlane](ConstructionPlaneDefinition_parentConstructionPlane.htm), [ConstructionPlaneDistanceOnPathDefinition.parentConstructionPlane](ConstructionPlaneDistanceOnPathDefinition_parentConstructionPlane.htm), [ConstructionPlaneMidplaneDefinition.parentConstructionPlane](ConstructionPlaneMidplaneDefinition_parentConstructionPlane.htm), [ConstructionPlaneOffsetDefinition.parentConstructionPlane](ConstructionPlaneOffsetDefinition_parentConstructionPlane.htm), [ConstructionPlaneOffsetThroughPointDefinition.parentConstructionPlane](ConstructionPlaneOffsetThroughPointDefinition_parentConstructionPlane.htm), [ConstructionPlanes.add](ConstructionPlanes_add.htm), [ConstructionPlanes.item](ConstructionPlanes_item.htm), [ConstructionPlanes.itemByName](ConstructionPlanes_itemByName.htm), [ConstructionPlaneTangentAtPointDefinition.parentConstructionPlane](ConstructionPlaneTangentAtPointDefinition_parentConstructionPlane.htm), [ConstructionPlaneTangentDefinition.parentConstructionPlane](ConstructionPlaneTangentDefinition_parentConstructionPlane.htm), [ConstructionPlaneThreePointsDefinition.parentConstructionPlane](ConstructionPlaneThreePointsDefinition_parentConstructionPlane.htm), [ConstructionPlaneTwoEdgesDefinition.parentConstructionPlane](ConstructionPlaneTwoEdgesDefinition_parentConstructionPlane.htm), [FlatPatternComponent.xYConstructionPlane](FlatPatternComponent_xYConstructionPlane.htm), [FlatPatternComponent.xZConstructionPlane](FlatPatternComponent_xZConstructionPlane.htm), [FlatPatternComponent.yZConstructionPlane](FlatPatternComponent_yZConstructionPlane.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Construction Plane API Sample](ConstructionPlaneSample_Sample.htm) | Demonstrates creating construction plane by different ways. |
| [Loft Feature API Sample](LoftFeatureSample_Sample.htm) | Demonstrates creating a new loft feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |