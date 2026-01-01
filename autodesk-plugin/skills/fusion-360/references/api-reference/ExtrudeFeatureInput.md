# ExtrudeFeatureInput Object

Derived from: [Base](Base.htm) Object

Defined in namespace "adsk::fusion" and the header file is <Fusion/Features/ExtrudeFeatureInput.h>

## Description

This class defines the methods and properties that pertain to the definition of an extrude feature. This class also provides properties for setting/getting the Profile and Operation of the extrude. The Profile and Operation are defined when the ExtrudeFeatures.createInput method is called so they do not exist as properties on this class.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [classType](ExtrudeFeatureInput_classType.htm) | Static function that all classes support that returns the type of the class as a string. The returned string matches the string returned by the objectType property. For example if you have a reference to an object and you want to check if it's a SketchLine you can use myObject.objectType == fusion.SketchLine.classType(). |
| [setAllExtent](ExtrudeFeatureInput_setAllExtent.htm) | \*\*RETIRED\*\* Sets the extrusion extents option to 'All' (i.e. the extrusion is through-all, in both directions.) This method will fail in the case of a non-parametric extrusion. |
| [setDistanceExtent](ExtrudeFeatureInput_setDistanceExtent.htm) | \*\*RETIRED\*\* Sets the extrusion extents option to 'Distance'. |
| [setOneSideExtent](ExtrudeFeatureInput_setOneSideExtent.htm) | Defines the extrusion to go in one direction from the profile. The extent of the extrusion is defined by the extent argument. |
| [setOneSideToExtent](ExtrudeFeatureInput_setOneSideToExtent.htm) | \*\*RETIRED\*\* Sets the extrusion Direction option to 'One Side' and the Extents option to 'To' (a specified face) |
| [setSymmetricExtent](ExtrudeFeatureInput_setSymmetricExtent.htm) | Defines the extrusion to go symmetrically in both directions from the profile. |
| [setThinExtrude](ExtrudeFeatureInput_setThinExtrude.htm) | Changes the extrude feature to be a thin extrude. This is only valid if the isThinExtrude property is False. If the extrusion is already a thin extrude, you can use the properties on the ExtrudeFeature to modify the thin extrude specific values. |
| [setTwoSidesDistanceExtent](ExtrudeFeatureInput_setTwoSidesDistanceExtent.htm) | \*\*RETIRED\*\* Sets the extrusion extents option to 'Two Side'. This method will fail in the case of a non-parametric extrusion. |
| [setTwoSidesExtent](ExtrudeFeatureInput_setTwoSidesExtent.htm) | Defines the extrusion to go in both directions from the profile. The extent is defined independently for each direction using the input arguments. |
| [setTwoSidesToExtent](ExtrudeFeatureInput_setTwoSidesToExtent.htm) | \*\*RETIRED\*\* Set the extrusion Direction option to 'Two Side'. This method will fail in the case of a non-parametric extrusion. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [creationOccurrence](ExtrudeFeatureInput_creationOccurrence.htm) | In order for geometry to be transformed correctly, an Occurrence for creation needs to be specified when the Extrusion is created based on geometry (e.g. a profile and/or face(s)) in another component AND (the Extrusion) is not in the root component. The CreationOccurrence is analogous to the active occurrence in the UI |
| [extentOne](ExtrudeFeatureInput_extentOne.htm) | Gets the extent assigned for a single sided extrude or side one of a two-sided extrusion. To set the extent, use one of the set methods on the ExtrudeFeatureInput object. |
| [extentTwo](ExtrudeFeatureInput_extentTwo.htm) | Gets the extent assigned for side two of the extrusion. If the extrude is single sided extrude this property will return null. The hasTwoExtents property can be used to determine if there are two sides or not. To set the extent, use one of the set methods on the ExtrudeFeatureInput object. |
| [hasTwoExtents](ExtrudeFeatureInput_hasTwoExtents.htm) | Property that indicates if the extrusion is a single or two-sided extrusion. If false, the extentTwo and taperAngleTwo properties should not be used. |
| [isSolid](ExtrudeFeatureInput_isSolid.htm) | Specifies if the extrusion should be created as a solid or surface. If it's a surface then there aren't any end caps and it's open. When an ExtrudeFeature input is created, this is initialized to true so a solid will be created if it's not changed. |
| [isThinExtrude](ExtrudeFeatureInput_isThinExtrude.htm) | Sets or returns whether the extrude is a thin extrude. Setting it as false will make it a regular extrude. |
| [isValid](ExtrudeFeatureInput_isValid.htm) | Indicates if this object is still valid, i.e. hasn't been deleted or some other action done to invalidate the reference. |
| [objectType](ExtrudeFeatureInput_objectType.htm) | This property is supported by all objects in the API and returns a string that contains the full name (namespace::objecttype) describing the type of the object. |
| [operation](ExtrudeFeatureInput_operation.htm) | Gets and sets the type of operation performed by the extrusion. |
| [participantBodies](ExtrudeFeatureInput_participantBodies.htm) | Gets and sets the list of bodies that will participate in the feature when the operation is a cut or intersection.   If this property has not been set, the default behavior is that all bodies that are intersected by the feature will participate.   This property can return null in the case where the feature has not been fully defined so that possible intersecting bodies can be computed. |
| [profile](ExtrudeFeatureInput_profile.htm) | Gets and sets the profiles or planar faces used to define the shape of the extrude. This property can return or be set with a single profile, a single planar face, or an ObjectCollection consisting of multiple profiles and planar faces. When an ObjectCollection is used all of the profiles and faces must be co-planar.   To create a surface (non-solid) extrusion, you can use the createOpenProfile and createBRepEdgeProfile methods of the Component object to create an open profile. The isSolid property of the ExtrudeFeatureInput property must also be False. |
| [startExtent](ExtrudeFeatureInput_startExtent.htm) | Gets and sets the extent used to define the start of the extrusion. When a new ExtrudeFeatureInput object is created the start extent is initialized to be the profile plane but you can change it to a profile plane with offset or from an object by setting this property with either a OffsetStartDefinition or an EntityStartDefinition object. You can get either one of those objects by using the static create method on the class. |
| [taperAngle](ExtrudeFeatureInput_taperAngle.htm) | \*\*RETIRED\*\* Gets and sets the taper angle of the extrusion. This is used to define the taper angle for a single sided and symmetric and defines the angle for side one of a two sided extrusion. This property is initialized with a taper angle of zero. A negative angle will taper the extrusion inward while a positive value will taper the extrusion outward. This property is valid for both parametric and non-parametric extrusions. |
| [taperAngleOne](ExtrudeFeatureInput_taperAngleOne.htm) | Gets the value that will be used as the taper angle for a single sided extrusion or side one of a two-sided extrusion. To set the taper angle, use one of the set methods on the ExtrudeFeatureInput object. |
| [taperAngleTwo](ExtrudeFeatureInput_taperAngleTwo.htm) | Gets the value that will be used as the taper angle for side two of a two-sided extrusion. If the extrusion is single-sided, this property will return null. The hasTwoExtents property can be used to determine if there are two sides or not. To set the taper angle, use one of the set methods on the ExtrudeFeatureInput object. |
| [targetBaseFeature](ExtrudeFeatureInput_targetBaseFeature.htm) | When creating a feature that is owned by a base feature, set this property to the base feature you want to associate the new feature with. By default, this is null, meaning it will not be associated with a base feature.   Because of a current limitation, if you want to create a feature associated with a base feature, you must set this property AND call the startEdit method of the base feature, create the feature, and then call the finishEdit method of the base feature. The base feature must be in an "edit" state to be able to add any additional items to it. |
| [thinExtrudeWallLocationOne](ExtrudeFeatureInput_thinExtrudeWallLocationOne.htm) | Gets and sets the wall location for a one sided thin extrude or side one of a two sided thin extrude |
| [thinExtrudeWallLocationTwo](ExtrudeFeatureInput_thinExtrudeWallLocationTwo.htm) | Gets and sets the wall location for side two of a two sided thin extrude |
| [thinExtrudeWallThicknessOne](ExtrudeFeatureInput_thinExtrudeWallThicknessOne.htm) | Gets and sets the wall thickness for a one sided thin extrude or side one of a two sided thin extrude |
| [thinExtrudeWallThicknessTwo](ExtrudeFeatureInput_thinExtrudeWallThicknessTwo.htm) | Gets and sets the wall thickness for side two of a two sided thin extrude |

## Accessed From

[ExtrudeFeatures.createInput](ExtrudeFeatures_createInput.htm)

## Samples

|  |  |
| --- | --- |
| Name | Description |
| [Extrude Feature API Sample](ExtrudeFeatureSample_Sample.htm) | Demonstrates creating a new extrude feature. |
| [Manage Participant Bodies API Sample](ParticipantBodiesSample_Sample.htm) | Demonstrates how to manage participant During Cut operation. Same API can be used to manage participants During intersection also. |

## Version

Introduced in version August 2014

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |