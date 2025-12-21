# ChamferFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The ChamferFeature object represents chamfered modeling features.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ChamferFeature/ChamferFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ChamferFeature/ChamferFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ChamferFeature/ChamferFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ChamferFeature/ChamferFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ChamferFeature/ChamferFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ChamferFeature/ChamferFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ChamferFeature/ChamferFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ChamferFeature/ChamferFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ChamferFeature/ChamferFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ChamferFeature/ChamferFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ChamferFeature/ChamferFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ChamferFeature/ChamferFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../ChamferFeature/ChamferFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../ChamferFeature/ChamferFeature_Definition.md) | Property that returns the ChamferDefinition object that defines how the chamfer is defined. The type of definition object that will be returned can be determined by using the DefinitionType property. |
| [ExtendedName](../ChamferFeature/ChamferFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ChamferFeature/ChamferFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ChamferFeature/ChamferFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ChamferFeature/ChamferFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../ChamferFeature/ChamferFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ChamferFeature/ChamferFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../ChamferFeature/ChamferFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ChamferFeature/ChamferFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ChamferFeature/ChamferFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ChamferFeature/ChamferFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ChamferFeature/ChamferFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ChamferFeature/ChamferFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../ChamferFeature/ChamferFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ChamferFeature/ChamferFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ChamferFeature/ChamferFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ChamferFeatureProxy.NativeObject](../ChamferFeatureProxy/ChamferFeatureProxy_NativeObject.md), [ChamferFeatures.AddUsingDistance](../ChamferFeatures/ChamferFeatures_AddUsingDistance.md), [ChamferFeatures.AddUsingDistanceAndAngle](../ChamferFeatures/ChamferFeatures_AddUsingDistanceAndAngle.md), [ChamferFeatures.AddUsingTwoDistances](../ChamferFeatures/ChamferFeatures_AddUsingTwoDistances.md), [ChamferFeatures.Item](../ChamferFeatures/ChamferFeatures_Item.md)

## Derived Classes

[ChamferFeatureProxy](../ChamferFeatureProxy/ChamferFeatureProxy.md)

## Version

Introduced in version 5

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |