# BossFeature Object

Derived from: [Feature](Feature.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeature.h>

## Description

Object that represents an existing boss feature in a design. For history free model this interface has limited functionality.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BossFeature_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [createForAssemblyContext](BossFeature_createForAssemblyContext.htm) | Creates or returns a proxy for the native object - i.e. a new object that represents this object but adds the assembly context defined by the input occurrence. |
| [createInput](BossFeature_createInput.htm) | Creates object with inputs this feature represents. To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True). |
| [deleteMe](BossFeature_deleteMe.htm) | Deletes the feature. This works for both parametric and non-parametric features. |
| [dissolve](BossFeature_dissolve.htm) | Dissolves the feature so that the feature information is lost and only the B-Rep geometry defined by the feature remains. This is only valid for non-parametric features. |
| [update](BossFeature_update.htm) | Changes the boss feature (or boss connection) to the input provided. To use this property, you need to position the timeline marker to immediately before this feature. This can be accomplished using the following code: thisFeature.timelineObject.rollTo(True). |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [alignmentDepth](BossFeature_alignmentDepth.htm) | Returns the model parameter controlling the step depth used for alignment of its counterparts. |
| [alignmentDiameter](BossFeature_alignmentDiameter.htm) | Returns the model parameter controlling the step diameter used for alignment of its counterparts. |
| [alignmentDraftAngle](BossFeature_alignmentDraftAngle.htm) | Returns the model parameter controlling the step draft angle. |
| [alignmentRootRadius](BossFeature_alignmentRootRadius.htm) | Returns the model parameter controlling blend radius of the boss alignment root. |
| [alignmentTipRadius](BossFeature_alignmentTipRadius.htm) | Returns the model parameter controlling blend radius of the boss alignment top face. |
| [alignmentType](BossFeature_alignmentType.htm) | Returns the current boss alignment shape this feature represents. |
| [assemblyContext](BossFeature_assemblyContext.htm) | Returns the assembly occurrence (i.e. the occurrence) of this object in an assembly. This is only valid in the case where this is acting as a proxy in an assembly. Returns null in the case where the object is not in the context of an assembly but is already the native object. |
| [attributes](BossFeature_attributes.htm) | Returns the collection of attributes associated with this face. |
| [baseFeature](BossFeature_baseFeature.htm) | If this feature is associated with a base feature, this property will return that base feature. If it's not associated with a base feature, this property will return null. |
| [bodies](BossFeature_bodies.htm) | Returns the bodies that were modified or created by this feature. This property works for both parametric and non-parametric features. |
| [diameter](BossFeature_diameter.htm) | Returns the model parameter controlling the shank diameter. |
| [direction](BossFeature_direction.htm) | Returns the direction of the boss feature with respect to selected position point. For selected sketch point this direction represents a Z-axis of the sketch. |
| [draftAngle](BossFeature_draftAngle.htm) | Returns the model parameter controlling the shank draft angle. |
| [entityToken](BossFeature_entityToken.htm) | Returns a token for the Feature object. This can be saved and used at a later time with the Design.findEntityByToken method to get back the same feature.   When using entity tokens it's important to understand that the token string returned for a specific entity can be different over time. However, even if you have two different token strings that were obtained from the same entity, when you use findEntityByToken they will both return the same entity. Because of that you should never compare entity tokens as way to determine what the token represents. Instead, you need to use the findEntityByToken method to get the two entities identified by the tokens and then compare them. |
| [errorOrWarningMessage](BossFeature_errorOrWarningMessage.htm) | Returns the error or warning message in the case where the healthState property returns either WarningFeatureHealthState or ErrorFeatureHealthState. Otherwise this property returns an empty string. |
| [faces](BossFeature_faces.htm) | Returns the faces that were created by this feature. This works for both parametric and non-parametric features.   Depending on the modifications made to the body after the feature was created, this may not return all of the faces. For example, when a component is created from a body, the original body and its faces no longer exist, so this won't return any faces. However, you can roll the timeline to immediately after the feature, and all the original faces will be available. |
| [healthState](BossFeature_healthState.htm) | Returns the current health state of the feature. |
| [holeCountersinkAngle](BossFeature_holeCountersinkAngle.htm) | Returns the model parameter controlling countersink angle for countersink hole. If hole type is not set to countersink hole or boss shape is to BossBlank this parameter is unused. |
| [holeDepth](BossFeature_holeDepth.htm) | Returns the model parameter controlling the hole depth with respect to hole extent type. If hole extent type is set to BossHoleThrough parameter not used. If hole extent type is BossBlindFull the parameter is a distance from farthest face. If hole extent type is set to BossBlindDepth the parameter is a distance from start face of the hole. |
| [holeDiameter](BossFeature_holeDiameter.htm) | Returns the model parameter controlling the hole diameter. |
| [holeDraftAngle](BossFeature_holeDraftAngle.htm) | Returns the model parameter controlling hole draft angle. |
| [holeEndRadius](BossFeature_holeEndRadius.htm) | Returns the model parameter controlling blend radius of the hole end. |
| [holeExtentType](BossFeature_holeExtentType.htm) | Returns the current type of hole extent this feature represents. |
| [holeMajorDepth](BossFeature_holeMajorDepth.htm) | Returns the model parameter controlling major hole depth for counterbore and countersink hole. If hole type is set to simple hole or boss shape is to BossBlank this parameter is unused. |
| [holeMajorDiameter](BossFeature_holeMajorDiameter.htm) | Returns the model parameter controlling major hole diameter for counterbore and countersink hole. If hole type is set to simple hole or boss shape is to BossBlank this parameter is unused. |
| [holeMajorDraftAngle](BossFeature_holeMajorDraftAngle.htm) | Returns the model parameter controlling major hole draft angle for counterbore and countersink hole. If hole type is set to simple hole or boss shape is to BossBlank this parameter is unused. |
| [holeMajorRootRadius](BossFeature_holeMajorRootRadius.htm) | Returns the model parameter controlling blend radius of major hole counterbore root. |
| [holeMajorTipRadius](BossFeature_holeMajorTipRadius.htm) | Returns the model parameter controlling blend radius of major hole counterbore. |
| [holeStartRadius](BossFeature_holeStartRadius.htm) | Returns the model parameter controlling blend radius of the hole start. |
| [holeType](BossFeature_holeType.htm) | Returns the current type of hole this feature represents. |
| [innerRadius](BossFeature_innerRadius.htm) | Returns the model parameter for inner radius - reference for parametric expressions. |
| [isDirectionFlipped](BossFeature_isDirectionFlipped.htm) | Gets and sets if the direction of the boss (or boss connection) is flipped. |
| [isGeometryOpposite](BossFeature_isGeometryOpposite.htm) | Gets if this boss feature instance represents a bottom side where screw thread engages with the part. If this feature instance represents a geometry where screw head engages it returns false. |
| [isParametric](BossFeature_isParametric.htm) | Indicates if this feature is parametric or not. |
| [isSuppressed](BossFeature_isSuppressed.htm) | Gets and sets if this feature is suppressed. This is only valid for parametric features. |
| [isValid](BossFeature_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [linkedFeatures](BossFeature_linkedFeatures.htm) | Returns the set of features that are linked to this feature. The set of linked features are all of the features that were created in various components as the result of a single feature being created in the user interface. |
| [name](BossFeature_name.htm) | Returns the name of the feature as seen in the browser (non-parametric) or in the timeline (parametric). |
| [nativeObject](BossFeature_nativeObject.htm) | The NativeObject is the object outside the context of an assembly and in the context of its parent component. Returns null in the case where this object is not in the context of an assembly but is already the native object. |
| [objectType](BossFeature_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object.   It's often useful to use this in combination with the classType method to see if an object is a certain type. For example: if obj.objectType == adsk.core.Point3D.classType(): |
| [offset](BossFeature_offset.htm) | Returns the model parameter controlling the offset from the selected parting plane. |
| [offsetClearance](BossFeature_offsetClearance.htm) | Returns the model parameter controlling the offset clearance from the selected parting plane and offset. |
| [parentComponent](BossFeature_parentComponent.htm) | Returns the parent component that owns this feature. |
| [positionDefinition](BossFeature_positionDefinition.htm) | Returns a BossPositionDefinition object that provides access to the information used to define the position of the boss feature. |
| [ribBlendRadius](BossFeature_ribBlendRadius.htm) | Returns the model parameter controlling size of rib root blend radius. |
| [ribChamferAngle](BossFeature_ribChamferAngle.htm) | Returns the model parameter controlling size of rib chamfer angle. |
| [ribCount](BossFeature_ribCount.htm) | Returns the model parameter controlling number of ribs. |
| [ribCutSize](BossFeature_ribCutSize.htm) | Returns the model parameter controlling size of rib chamfer or fillet. |
| [ribDraftAngle](BossFeature_ribDraftAngle.htm) | Returns the model parameter controlling ribs draft angle. |
| [ribLength](BossFeature_ribLength.htm) | Returns the model parameter controlling ribs length measured from the shank axis. |
| [ribOffset](BossFeature_ribOffset.htm) | Returns the model parameter controlling ribs offset from the top face or alignment face. |
| [ribOuterDraftAngle](BossFeature_ribOuterDraftAngle.htm) | Returns the model parameter controlling size of rib outer draft angle. |
| [ribRotation](BossFeature_ribRotation.htm) | Returns the model parameter controlling rotation angle of the first rib from the reference vector. For selected sketch point(s) the direction of reference vector is X-axis of the parent sketch. |
| [ribThickness](BossFeature_ribThickness.htm) | Returns the model parameter controlling ribs thickness. |
| [ribTipRadius](BossFeature_ribTipRadius.htm) | Returns the model parameter controlling size of rib tip blend radius. |
| [ribTotalAngle](BossFeature_ribTotalAngle.htm) | Returns the model parameter controlling total angle for ribs distribution. |
| [ribType](BossFeature_ribType.htm) | Returns the current type of ribs shape this feature represents. |
| [rootRadius](BossFeature_rootRadius.htm) | Returns the model parameter controlling blend radius of the boss shank. |
| [screwDiameter](BossFeature_screwDiameter.htm) | Returns the model parameter for screw diameter - reference for parametric expressions. |
| [screwHeadAngle](BossFeature_screwHeadAngle.htm) | Returns the model parameter for countersink head angle - reference for parametric expressions. |
| [screwHeadDiameter](BossFeature_screwHeadDiameter.htm) | Returns the model parameter for screw head diameter - reference for parametric expressions. |
| [shapeType](BossFeature_shapeType.htm) | Returns the current boss shape this feature represents. |
| [taperAngle](BossFeature_taperAngle.htm) | Returns the model parameter for taper angle - plastic part rule reference. |
| [thickness](BossFeature_thickness.htm) | Returns the model parameter for thickness - plastic part rule reference. |
| [timelineObject](BossFeature_timelineObject.htm) | Returns the timeline object associated with this feature. |
| [tipRadius](BossFeature_tipRadius.htm) | Returns the model parameter controlling blend radius of the boss shank top face. |

## Accessed From

[BossFeature.createForAssemblyContext](BossFeature_createForAssemblyContext.htm), [BossFeature.nativeObject](BossFeature_nativeObject.htm), [BossFeatures.add](BossFeatures_add.htm), [BossFeatures.item](BossFeatures_item.htm), [BossFeatures.itemByName](BossFeatures_itemByName.htm)

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |