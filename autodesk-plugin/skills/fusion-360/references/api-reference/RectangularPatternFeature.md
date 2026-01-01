# RectangularPatternFeature Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/RectangularPatternFeature.h>

## Description

Object that represents an existing rectangular pattern feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](RectangularPatternFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](RectangularPatternFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](RectangularPatternFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](RectangularPatternFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](RectangularPatternFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](RectangularPatternFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](RectangularPatternFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](RectangularPatternFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [directionOne](RectangularPatternFeature_directionOne.htm) | Returns a Vector3D indicating the positive direction of direction one. |
| [directionOneEntity](RectangularPatternFeature_directionOneEntity.htm) | Gets and sets the first direction entity. This can be a linear edge, construction axis, sketch line or rectangular pattern feature. If a rectangular pattern feature is set, the directionOneEntity and directionTwoEntity properties return the same rectangular pattern feature.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [directionTwo](RectangularPatternFeature_directionTwo.htm) | Returns a Vector3D indicating the positive direction of direction two. |
| [directionTwoEntity](RectangularPatternFeature_directionTwoEntity.htm) | Gets and sets the second direction entity. This can be a linear edge, construction axis, sketch line or rectangular pattern feature. If a rectangular pattern feature is set, the directionOneEntity and directionTwoEntity properties return the same rectangular pattern feature. This can be null when not entity has been specified to control the second direction. In this case Fusion will compute a default direction which is 90 degrees to the direction one.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [distanceOne](RectangularPatternFeature_distanceOne.htm) | Gets the distance in the first direction. Edit the value through ModelParameter. Returns nothing in the case where the feature is non-parametric. |
| [distanceTwo](RectangularPatternFeature_distanceTwo.htm) | Gets the distance in the second direction. Edit the value through ModelParameter. Returns nothing in the case where the feature is non-parametric. |
| [entityToken](RectangularPatternFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](RectangularPatternFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](RectangularPatternFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](RectangularPatternFeature_healthState.htm) | Returns the current health state of the feature. |
| [inputEntities](RectangularPatternFeature_inputEntities.htm) | Gets and sets the input entities. The collection can contain faces, features, bodies or occurrences. All of the entities must be of a single type. For example, it can't contain features and occurrences but only features or occurrences.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isParametric](RectangularPatternFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](RectangularPatternFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isSymmetricInDirectionOne](RectangularPatternFeature_isSymmetricInDirectionOne.htm) | Gets and sets if the pattern in direction one is in one direction or symmetric.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isSymmetricInDirectionTwo](RectangularPatternFeature_isSymmetricInDirectionTwo.htm) | Gets and sets if the pattern in direction two is in one direction or symmetric.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [isValid](RectangularPatternFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](RectangularPatternFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](RectangularPatternFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](RectangularPatternFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](RectangularPatternFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](RectangularPatternFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [patternComputeOption](RectangularPatternFeature_patternComputeOption.htm) | Gets and sets the compute option for this pattern feature. This property only applies when patterning features and is ignored in the direct modeling environment.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [patternDistanceType](RectangularPatternFeature_patternDistanceType.htm) | Gets and sets how the distance between elements is computed. Is initialized to ExtentPatternDistanceType when a new RectangularPatternFeatureInput has been created.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [patternElements](RectangularPatternFeature_patternElements.htm) | Gets the PatternElements collection that contains the elements created by this pattern. |
| [patternEntityType](RectangularPatternFeature_patternEntityType.htm) | Returns the type of entities the pattern consists of. This can be used to help determine the type of results that will be found in the pattern elements. |
| [quantityOne](RectangularPatternFeature_quantityOne.htm) | Gets the number of instances in the first direction. Edit the value through ModelParameter. Returns nothing in the case where the feature is non-parametric. |
| [quantityTwo](RectangularPatternFeature_quantityTwo.htm) | Gets the number of instances in the second direction. Edit the value through ModelParameter. Returns nothing in the case where the feature is non-parametric. |
| [resultFeatures](RectangularPatternFeature_resultFeatures.htm) | Get the features that were created for this pattern. Returns null in the case where the feature is parametric. |
| [suppressedElementsIds](RectangularPatternFeature_suppressedElementsIds.htm) | Gets and sets the ids of the patterns to suppress.   To set this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [timelineObject](RectangularPatternFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |

## Accessed From

[RectangularPatternFeature.createForAssemblyContext](RectangularPatternFeature_createForAssemblyContext.htm), [RectangularPatternFeature.nativeObject](RectangularPatternFeature_nativeObject.htm), [RectangularPatternFeatures.add](RectangularPatternFeatures_add.htm), [RectangularPatternFeatures.item](RectangularPatternFeatures_item.htm), [RectangularPatternFeatures.itemByName](RectangularPatternFeatures_itemByName.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |
| [RectangularPattern Feature](RectangularPatternFeatureSample_Sample.htm) | Demonstrates creating a new rectangular pattern feature. |

## Version

Introduced in version November 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |