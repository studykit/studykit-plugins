# HoleFeature Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/HoleFeature.h>

## Description

Object that represents an existing hole feature in a design.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](HoleFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](HoleFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [deleteMe](HoleFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](HoleFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |
| [setAllExtent](HoleFeature_setAllExtent.htm) | Defines the extent of the hole to be through-all. The direction can be either positive, negative. |
| [setDistanceExtent](HoleFeature_setDistanceExtent.htm) | Defines the depth of the hole using a specific distance.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setOneSideToExtent](HoleFeature_setOneSideToExtent.htm) | Sets the extent of the hole to be from the sketch plane to the specified "to" face.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setPositionAtCenter](HoleFeature_setPositionAtCenter.htm) | Redefines the position of the hole at the center of a circular or elliptical edge of the face.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setPositionByPlaneAndOffsets](HoleFeature_setPositionByPlaneAndOffsets.htm) | Redefines the orientation of the hole using a planar face or construction plane. The position of the hole is defined by the distance from one or two edges.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setPositionByPoint](HoleFeature_setPositionByPoint.htm) | Redefines the position of a the hole using a point. The point can be a vertex on the face or it can be a Point3D object to define any location on the face. If a Point3D object is provided it will be projected onto the plane along the planes normal. The orientation of the hole is defined by the planar face or construction plane. If a vertex is used, the position of the hole is associative to that vertex. If a Point3D object is used the position of the hole is not associative.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setPositionBySketchPoint](HoleFeature_setPositionBySketchPoint.htm) | Redefines the position and orientation of the hole using a sketch point.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setPositionBySketchPoints](HoleFeature_setPositionBySketchPoints.htm) | Redefines the position and orientation of the hole using a set of points.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setPositionOnEdge](HoleFeature_setPositionOnEdge.htm) | Redefines the position and orientation of the hole to be on the start, end or center of an edge.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setToClearanceHole](HoleFeature_setToClearanceHole.htm) | Sets the hole to be a clearance hole of the size specified by the ClearanceHoleInfo object. |
| [setToCounterbore](HoleFeature_setToCounterbore.htm) | Calling this method will change the hole to a counterbore hole.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setToCountersink](HoleFeature_setToCountersink.htm) | Calling this method will change the hole to a countersink hole.   To use this method, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [setToSimple](HoleFeature_setToSimple.htm) | Calling this method will change the hole to a simple hole. |
| [setToSimpleHole](HoleFeature_setToSimpleHole.htm) | This method sets the hole's tap to be "simple," which means that the hole will not have any tap and will be a simple hole. |
| [setToTappedHole](HoleFeature_setToTappedHole.htm) | Sets the hole to be a straight or tapered tapped hole of the size specified by the ThreadInfo object. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [assemblyContext](HoleFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](HoleFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](HoleFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](HoleFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features.   For a BaseFeature, this property has two different behaviors depending on if the BaseFeature is active for edit or not. When the base feature is active, this property returns the bodies owned by the base feature or the source bodies. When the base feature is not active, this property returns the result bodies.   When a body is added to a base feature, that body is owned by the base feature and is only seen in the UI when the base feature is active. This body is referred to as a "source body". Fusion creates a parametric copy of the body when you exit the base feature. This copy is referred to as the "result body," and it is used for subsequent modeling operations.   You can map between the source and result bodies by using their position within the bodies returned. To get a valid list of result bodies, you should roll the timeline to immediately after the base feature node in the timeline. Otherwise, subsequent operations could have done something to cause one or more bodies to no longer be available. |
| [clearanceHoleInfo](HoleFeature_clearanceHoleInfo.htm) | Returns the information used to define a clearance hole. This returns a ClearanceHoleInfo object when the holeTapType returns ClearanceHoleTapType. Otherwise this property returns null. |
| [counterboreDepth](HoleFeature_counterboreDepth.htm) | Returns the model parameter controlling the counterbore depth. This will return null in the case the hole type is not a counterbore. The depth of the counterbore can be edited through the returned parameter. |
| [counterboreDiameter](HoleFeature_counterboreDiameter.htm) | Returns the model parameter controlling the counterbore diameter. This will return null in the case the hole type is not a counterbore. The diameter of the counterbore can be edited through the returned parameter. |
| [countersinkAngle](HoleFeature_countersinkAngle.htm) | Returns the model parameter controlling the countersink angle. This will return null in the case the hole type is not a countersink. The angle of the countersink can be edited through the returned parameter. |
| [countersinkDiameter](HoleFeature_countersinkDiameter.htm) | Returns the model parameter controlling the countersink diameter. This will return null in the case the hole type is not a countersink. The diameter of the countersink can be edited through the returned parameter. |
| [direction](HoleFeature_direction.htm) | Returns the direction of the hole. |
| [endFaces](HoleFeature_endFaces.htm) | Property that returns the faces at the bottom of the hole. This will typically be a single face but could return more than one face in the case where the bottom of the hole is uneven. |
| [entityToken](HoleFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](HoleFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [extentDefinition](HoleFeature_extentDefinition.htm) | Gets the definition object that is defining the extent of the hole. Modifying the definition object will cause the hole to recompute. The extent type of a hole is currently limited to a distance extent. |
| [faces](HoleFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](HoleFeature_healthState.htm) | Returns the current health state of the feature. |
| [holeDiameter](HoleFeature_holeDiameter.htm) | Returns the model parameter controlling the hole diameter. The diameter of the hole can be edited through the returned parameter object.   If there is a thread associated with the hole the thread definition controls the diameter of the hole. Even though there is a parameter for the diameter, its value is ignored when there is a thread. |
| [holePositionDefinition](HoleFeature_holePositionDefinition.htm) | Returns a HolePositionDefinition object that provides access to the information used to define the position of the hole. This returns null in the case where IsParametric is false. |
| [holeTapType](HoleFeature_holeTapType.htm) | This property returns the current type of tap associated with this hole. You can set the tap type by using one of the following methods: setToSimpleHole, setToClearanceHole, or setToTappedHole. |
| [holeType](HoleFeature_holeType.htm) | Returns the current type of hole this feature represents. |
| [isDefaultDirection](HoleFeature_isDefaultDirection.htm) | Gets and sets if the hole is in the default direction or not. |
| [isParametric](HoleFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](HoleFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](HoleFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](HoleFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](HoleFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](HoleFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](HoleFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [parentComponent](HoleFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [participantBodies](HoleFeature_participantBodies.htm) | Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.   To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True) |
| [position](HoleFeature_position.htm) | Returns the position of the hole. |
| [sideFaces](HoleFeature_sideFaces.htm) | Property that returns all of the side faces of the hole. |
| [tappedHoleInfo](HoleFeature_tappedHoleInfo.htm) | This property returns the information used to define a tapped hole. Otherwise, this property returns null. |
| [thread](HoleFeature_thread.htm) | When a tapped hole is created, a thread feature is also automatically created and controls the tapped threads. The thread feature is tied to the hole and is not displayed in the timeline and is suppressed if the hole is suppressed and deleted if the hole is deleted. This property returns the thread feature associated with this hole if it is a tapped hole. It returns null for all other hole types. |
| [timelineObject](HoleFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [tipAngle](HoleFeature_tipAngle.htm) | Returns the model parameter controlling the angle of the tip of the hole. The tip angle of the hole can be edited through the returned parameter object. |

## Accessed From

[HoleFeature.createForAssemblyContext](HoleFeature_createForAssemblyContext.htm), [HoleFeature.nativeObject](HoleFeature_nativeObject.htm), [HoleFeatures.add](HoleFeatures_add.htm), [HoleFeatures.item](HoleFeatures_item.htm), [HoleFeatures.itemByName](HoleFeatures_itemByName.htm), [ThreadFeature.hole](ThreadFeature_hole.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Hole Feature API Sample](HoleFeatureSample_Sample.htm) | Demonstrates creating a new hole feature. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |