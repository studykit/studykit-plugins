# MirrorFeature Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/MirrorFeature.h>

## Description

Object that represents an existing mirror feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](MirrorFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](MirrorFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](MirrorFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](MirrorFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](MirrorFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](MirrorFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](MirrorFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](MirrorFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [entityToken](MirrorFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](MirrorFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](MirrorFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](MirrorFeature_healthState.htm) | Returns the current health state of the feature. |
| [inputEntities](MirrorFeature_inputEntities.htm) | Gets and sets the entities that are mirrored. It can contain faces, features, bodies, or components. The input must all be of a single type. For example, you can't provide a body and a component but the collection must be either all bodies or all components.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isCombine](MirrorFeature_isCombine.htm) | Gets and sets whether combine is set when doing the Mirror. When true, the mirrored geometry will be Boolean unioned with the original solid or surface body(s) when they connect within the stitch tolerance defined with the stitchTolerance property. If the bodies cannot be unioned or stitched the result will be separate bodies.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isParametric](MirrorFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](MirrorFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](MirrorFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](MirrorFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [mirrorPlane](MirrorFeature_mirrorPlane.htm) | Gets and sets the mirror plane. This can be either a planar face or construction plane. This works only for parametric features.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [name](MirrorFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](MirrorFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](MirrorFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](MirrorFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [patternComputeOption](MirrorFeature_patternComputeOption.htm) | Gets and sets the compute option for this mirror feature. This property only applies when mirroring features and is ignored in the direct modeling environment.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [patternElements](MirrorFeature_patternElements.htm) | Gets the PatternElements collection that contains the elements created by this pattern. |
| [resultFeatures](MirrorFeature_resultFeatures.htm) | Get the features that were created for this mirror. Returns null in the case where the feature is not parametric. |
| [stitchTolerance](MirrorFeature_stitchTolerance.htm) | Returns the parameter controlling the Stitch tolerance to use when stitching mirrored surface bodies with the original bodies. You can edit the tolerance by editing the value of the parameter object. |
| [timelineObject](MirrorFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |

## Accessed From

[MirrorFeature.createForAssemblyContext](MirrorFeature_createForAssemblyContext.htm), [MirrorFeature.nativeObject](MirrorFeature_nativeObject.htm), [MirrorFeatures.add](MirrorFeatures_add.htm), [MirrorFeatures.item](MirrorFeatures_item.htm), [MirrorFeatures.itemByName](MirrorFeatures_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Mirror Feature API Sample](MirrorFeatureSample_Sample.htm) | Demonstrates creating a new mirror feature |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |