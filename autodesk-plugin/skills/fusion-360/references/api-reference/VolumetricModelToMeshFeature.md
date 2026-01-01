# VolumetricModelToMeshFeature Object ![Preview](../images/TestTubeLarge.png)

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/VolumetricModelToMeshFeature.h>

![Preview](../images/TestTubeSmall.png)This functionality is provided as a preview
of intended future API capabilities. You are encouraged to use it and report any problems or suggestions using the
[Fusion API and Scripts](https://forums.autodesk.com/t5/fusion-360-api-and-scripts/bd-p/22) forum.

Because this is a preview of future functionality, there is the possibility that it will change, which will possibly
break any existing programs that use this functionality. Because of that, you should never deliver any programs that use
any preview capabilities. For a distributed program, you should wait until it has moved from preview to released state.

## Description

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](VolumetricModelToMeshFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](VolumetricModelToMeshFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](VolumetricModelToMeshFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](VolumetricModelToMeshFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](VolumetricModelToMeshFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](VolumetricModelToMeshFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](VolumetricModelToMeshFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](VolumetricModelToMeshFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [elementSize](VolumetricModelToMeshFeature_elementSize.htm) | Gets the element size that will be used when creating the mesh. This value is only used when the refinement type is set to Custom. The value must be greater than 0.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [entityToken](VolumetricModelToMeshFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](VolumetricModelToMeshFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](VolumetricModelToMeshFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](VolumetricModelToMeshFeature_healthState.htm) | Returns the current health state of the feature. |
| [isComputeSuspended](VolumetricModelToMeshFeature_isComputeSuspended.htm) | Gets and sets if the feature compute should be suspended if a dependent entity changes. If true, the feature will need to be recomputed manually if a dependent entity changes.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isParametric](VolumetricModelToMeshFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSmallShellsRemoved](VolumetricModelToMeshFeature_isSmallShellsRemoved.htm) | Gets and sets if small mesh shells should be removed after creating the mesh.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isSuppressed](VolumetricModelToMeshFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](VolumetricModelToMeshFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [isVolumetricModelRemoved](VolumetricModelToMeshFeature_isVolumetricModelRemoved.htm) | Gets and sets if the volumetric model should be removed after creating the mesh.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [linkedFeatures](VolumetricModelToMeshFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [meshBody](VolumetricModelToMeshFeature_meshBody.htm) | Get the mesh body created from the volumetric model. |
| [meshingApproach](VolumetricModelToMeshFeature_meshingApproach.htm) | Gets and sets the meshing approach to be used when creating the mesh.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [name](VolumetricModelToMeshFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](VolumetricModelToMeshFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](VolumetricModelToMeshFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](VolumetricModelToMeshFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [refinementType](VolumetricModelToMeshFeature_refinementType.htm) | Gets and sets the refinement type to be used when creating the mesh.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [smallShellThreshold](VolumetricModelToMeshFeature_smallShellThreshold.htm) | Gets the small mesh threshold used to determine if a mesh shell is considered small. The value is a fraction of the total mesh area and must be between 0 and 1.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [timelineObject](VolumetricModelToMeshFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [volumetricModel](VolumetricModelToMeshFeature_volumetricModel.htm) | Gets and sets the volumetric model to be converted to a mesh. The volumetric model must have the same parent component as the VolumetricModelToMeshFeature.This property is typed as core.Base because the adsk.fusion library does not reference the volume library where the VolumetricModel object is defined. At runtime, this property will return a VolumetricModel object.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |

## Accessed From

[VolumetricModelToMeshFeature.createForAssemblyContext](VolumetricModelToMeshFeature_createForAssemblyContext.htm), [VolumetricModelToMeshFeature.nativeObject](VolumetricModelToMeshFeature_nativeObject.htm), [VolumetricModelToMeshFeatures.add](VolumetricModelToMeshFeatures_add.htm), [VolumetricModelToMeshFeatures.item](VolumetricModelToMeshFeatures_item.htm), [VolumetricModelToMeshFeatures.itemByName](VolumetricModelToMeshFeatures_itemByName.htm)

## Version

Introduced in version May 2025

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |