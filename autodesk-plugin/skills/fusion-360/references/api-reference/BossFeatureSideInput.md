# BossFeatureSideInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Plastic/BossFeatureSideInput.h>

## Description

This class defines the methods and properties that pertain to the definition of a single side of boss feature

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](BossFeatureSideInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [clearRibExtent](BossFeatureSideInput_clearRibExtent.htm) | Clears rib extent types for all position points. |
| [setBlank](BossFeatureSideInput_setBlank.htm) | Set boss shape into blank constant diameter shank with no hole. |
| [setCounterbore](BossFeatureSideInput_setCounterbore.htm) | Set boss shape into constant diameter shank with counterbore hole. |
| [setCountersink](BossFeatureSideInput_setCountersink.htm) | Set boss shape into constant diameter shank with countersink hole. |
| [setRibExtent](BossFeatureSideInput_setRibExtent.htm) | Set rib extent type for particular rib for position point provided. |
| [setSimple](BossFeatureSideInput_setSimple.htm) | Set boss shape into constant diameter shank with simple hole. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [alignmentDepth](BossFeatureSideInput_alignmentDepth.htm) | Get or set alignment depth. |
| [alignmentDiameter](BossFeatureSideInput_alignmentDiameter.htm) | Get or set alignment diameter. |
| [alignmentDraftAngle](BossFeatureSideInput_alignmentDraftAngle.htm) | Get or set alignment draft angle. |
| [alignmentRootRadius](BossFeatureSideInput_alignmentRootRadius.htm) | Get or set blend radius of the boss alignment root. |
| [alignmentTipRadius](BossFeatureSideInput_alignmentTipRadius.htm) | Get or set blend radius of the boss alignment tip. |
| [alignmentType](BossFeatureSideInput_alignmentType.htm) | Get or set boss alignment shape. This usually corresponds to the alignment shape of the boss counterpart. |
| [diameter](BossFeatureSideInput_diameter.htm) | Get or set boss shank diameter. |
| [draftAngle](BossFeatureSideInput_draftAngle.htm) | Get or set shank draft angle. |
| [holeCountersinkAngle](BossFeatureSideInput_holeCountersinkAngle.htm) | Get or set countersink angle for countersink hole. This input is used only for countersink hole. |
| [holeDepth](BossFeatureSideInput_holeDepth.htm) | Get or set hole depth with respect to hole extent type. If hole extent type is set to BossHoleThrough parameter is ignored. If hole extent type is BossBlindFull the parameter is a distance from farthest face. If hole extent type is set to BossBlindDepth the parameter is a distance from start face of the hole. |
| [holeDiameter](BossFeatureSideInput_holeDiameter.htm) | Get or set hole diameter. |
| [holeDraftAngle](BossFeatureSideInput_holeDraftAngle.htm) | Get or set hole draft angle. |
| [holeEndRadius](BossFeatureSideInput_holeEndRadius.htm) | Get or set blend radius of the hole end. |
| [holeExtentType](BossFeatureSideInput_holeExtentType.htm) | Get or set hole extent this feature represents. For top side only through hole extent is accepted. |
| [holeMajorDepth](BossFeatureSideInput_holeMajorDepth.htm) | Get or set major hole depth for counterbore and countersink hole or material thickness under screw head based on hole orientation in a boss feature. This input is ignored for blank boss or boss with simple hole. |
| [holeMajorDiameter](BossFeatureSideInput_holeMajorDiameter.htm) | Get or set major hole diameter for counterbore or countersink hole. This input is ignored for blank boss or boss with simple hole. |
| [holeMajorDraftAngle](BossFeatureSideInput_holeMajorDraftAngle.htm) | Get or set major hole draft angle for counterbore and countersink hole. This input is ignored for blank boss or boss with simple hole. |
| [holeMajorRootRadius](BossFeatureSideInput_holeMajorRootRadius.htm) | Get or set blend radius of major hole counterbore root. |
| [holeMajorTipRadius](BossFeatureSideInput_holeMajorTipRadius.htm) | Get or set blend radius of major hole counterbore. |
| [holeStartRadius](BossFeatureSideInput_holeStartRadius.htm) | Get or set blend radius of the hole start. |
| [isValid](BossFeatureSideInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](BossFeatureSideInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [offsetClearance](BossFeatureSideInput_offsetClearance.htm) | Get or set offset clearance as additional small offset from the selected parting plane and position point. |
| [ribChamferAngle](BossFeatureSideInput_ribChamferAngle.htm) | Get or set rib chamfer angle. This input is used only for rib with chamfer. |
| [ribCount](BossFeatureSideInput_ribCount.htm) | Get or set number of ribs. |
| [ribCutSize](BossFeatureSideInput_ribCutSize.htm) | Get or set size of rib chamfer or fillet. |
| [ribDraftAngle](BossFeatureSideInput_ribDraftAngle.htm) | Get or set ribs draft angle. |
| [ribLength](BossFeatureSideInput_ribLength.htm) | Get or set ribs length measured from the shank axis. |
| [ribOffset](BossFeatureSideInput_ribOffset.htm) | Get or set ribs offset from the top face or alignment face. |
| [ribOuterDraftAngle](BossFeatureSideInput_ribOuterDraftAngle.htm) | Get or set rib outer draft angle. |
| [ribRootRadius](BossFeatureSideInput_ribRootRadius.htm) | Get or set rib base root blend radius. |
| [ribRotation](BossFeatureSideInput_ribRotation.htm) | Get or set rotation angle of the first rib from the reference vector. Reference vector is X-axis of the parent sketch from selected sketch point(s). |
| [ribThickness](BossFeatureSideInput_ribThickness.htm) | Get or set ribs thickness. |
| [ribTipRadius](BossFeatureSideInput_ribTipRadius.htm) | Get or set rib outer tip blend radius. |
| [ribTotalAngle](BossFeatureSideInput_ribTotalAngle.htm) | Get or set total angle for ribs distribution. Default is 360 deg. |
| [ribType](BossFeatureSideInput_ribType.htm) | Type of boss ribs this feature represents. |
| [rootRadius](BossFeatureSideInput_rootRadius.htm) | Get or set blend radius of the boss shank and participant body. |
| [tipRadius](BossFeatureSideInput_tipRadius.htm) | Get or set blend radius of the boss shank top parting face. |

## Accessed From

[BossFeatureInput.createSideInput](BossFeatureInput_createSideInput.htm), [BossFeatureInput.side1](BossFeatureInput_side1.htm), [BossFeatureInput.side2](BossFeatureInput_side2.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Boss Feature Sample](BossFeatureSample_Sample.htm) | Demonstrates creating a new boss feature |

## Version

Introduced in version October 2022

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |