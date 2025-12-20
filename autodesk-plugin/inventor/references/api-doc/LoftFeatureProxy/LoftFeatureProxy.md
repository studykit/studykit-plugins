# LoftFeatureProxy Object

Derived from: [LoftFeature](../LoftFeature/LoftFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../LoftFeatureProxy/LoftFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../LoftFeatureProxy/LoftFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../LoftFeatureProxy/LoftFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../LoftFeatureProxy/LoftFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../LoftFeatureProxy/LoftFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../LoftFeatureProxy/LoftFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../LoftFeatureProxy/LoftFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../LoftFeatureProxy/LoftFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../LoftFeatureProxy/LoftFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../LoftFeatureProxy/LoftFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../LoftFeatureProxy/LoftFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../LoftFeatureProxy/LoftFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../LoftFeatureProxy/LoftFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../LoftFeatureProxy/LoftFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../LoftFeatureProxy/LoftFeatureProxy_Definition.md) | Gets and sets the definition for the loft feature. |
| [EndFace](../LoftFeatureProxy/LoftFeatureProxy_EndFace.md) | Property that returns the that acts as the cap of the last section of the loft. This property will return nothing in the cases where the loft does not have a ending face. These cases are when the loft sections are not closed or when the loft operation does not result in a solid. |
| [ExtendedName](../LoftFeatureProxy/LoftFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../LoftFeatureProxy/LoftFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../LoftFeatureProxy/LoftFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../LoftFeatureProxy/LoftFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../LoftFeatureProxy/LoftFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../LoftFeatureProxy/LoftFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../LoftFeatureProxy/LoftFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../LoftFeatureProxy/LoftFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../LoftFeatureProxy/LoftFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../LoftFeatureProxy/LoftFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../LoftFeatureProxy/LoftFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../LoftFeatureProxy/LoftFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../LoftFeatureProxy/LoftFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../LoftFeatureProxy/LoftFeatureProxy_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [StartFace](../LoftFeatureProxy/LoftFeatureProxy_StartFace.md) | Property that returns the that acts as the cap of the first section of the loft. This property will return nothing in the cases where the loft does not have a starting face. These cases are when the loft sections are not closed or when the loft operation does not result in a solid. |
| [Suppressed](../LoftFeatureProxy/LoftFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../LoftFeatureProxy/LoftFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../LoftFeatureProxy/LoftFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |