# StitchFeature Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/StitchFeature.h>

## Description

Object that represents an existing stitch feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](StitchFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](StitchFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](StitchFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](StitchFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](StitchFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](StitchFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](StitchFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](StitchFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [entityToken](StitchFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](StitchFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](StitchFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](StitchFeature_healthState.htm) | Returns the current health state of the feature. |
| [isParametric](StitchFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](StitchFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](StitchFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](StitchFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](StitchFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](StitchFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](StitchFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [operation](StitchFeature_operation.htm) | Gets and sets the feature operation to perform. This property value is ignored if the stitched result does not form a solid body.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [parentComponent](StitchFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [stitchSurfaces](StitchFeature_stitchSurfaces.htm) | Gets and sets the surfaces to stitch together. In some cases the stitch operation results in faces being merged so the original faces are no longer available after the feature is created. in this case you need to reposition the timeline marker to just before this feature when the faces do exist.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [timelineObject](StitchFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [tolerance](StitchFeature_tolerance.htm) | Returns the parameter controlling the tolerance. You can edit the tolerance by editing the value of the parameter object. |

## Accessed From

[StitchFeature.createForAssemblyContext](StitchFeature_createForAssemblyContext.htm), [StitchFeature.nativeObject](StitchFeature_nativeObject.htm), [StitchFeatures.add](StitchFeatures_add.htm), [StitchFeatures.item](StitchFeatures_item.htm), [StitchFeatures.itemByName](StitchFeatures_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Stitch Feature API Sample](StitchFeatureSample_Sample.htm) | Demonstrates creating a new stitch feature. |

## Version

Introduced in version June 2015

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |