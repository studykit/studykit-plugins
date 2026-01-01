# UntrimFeature Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/UntrimFeature.h>

## Description

Object that represents an existing Untrim feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](UntrimFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](UntrimFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](UntrimFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](UntrimFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |
| [redefineLoops](UntrimFeature_redefineLoops.htm) | Set the loops to be removed. |
| [redefineLoopsFromFaces](UntrimFeature_redefineLoopsFromFaces.htm) | Set the loops to be removed from a set of faces. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](UntrimFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](UntrimFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](UntrimFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](UntrimFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [entityToken](UntrimFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](UntrimFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [extensionDistance](UntrimFeature_extensionDistance.htm) | Gets the ModelParameter that defines the extension distance used to extend external boundaries. This can return null in the case where only internal boundaries have been removed. The value can be edited by using the properties of the returned ModelParameter object. |
| [faces](UntrimFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [facesToUntrim](UntrimFeature_facesToUntrim.htm) | Gets the face objects to untrim. Returns null/None in the case where loops are specified instead of faces. |
| [healthState](UntrimFeature_healthState.htm) | Returns the current health state of the feature. |
| [isParametric](UntrimFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](UntrimFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](UntrimFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](UntrimFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [loopsToUntrim](UntrimFeature_loopsToUntrim.htm) | Gets the loop objects to untrim. Returns null/None in the case where faces are specified instead of loops |
| [name](UntrimFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](UntrimFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](UntrimFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](UntrimFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [timelineObject](UntrimFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [untrimLoopType](UntrimFeature_untrimLoopType.htm) | Gets the loop type that was untrimmed. To change the trim type, use one of the redefine methods. |

## Accessed From

[UntrimFeature.createForAssemblyContext](UntrimFeature_createForAssemblyContext.htm), [UntrimFeature.nativeObject](UntrimFeature_nativeObject.htm), [UntrimFeatures.add](UntrimFeatures_add.htm), [UntrimFeatures.item](UntrimFeatures_item.htm), [UntrimFeatures.itemByName](UntrimFeatures_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Untrim Feature API Sample](UntrimFeatureSample_Sample.htm) | Demonstrates creating a new untrim feature. |

## Version

Introduced in version January 2021

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |