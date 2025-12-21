# RuleFilletFeatureProxy Object

Derived from: [RuleFilletFeature](../RuleFilletFeature/RuleFilletFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [ExtendedName](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../RuleFilletFeatureProxy/RuleFilletFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2010
