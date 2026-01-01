# RuledSurfaceFeatureProxy Object

Derived from: [RuledSurfaceFeature](../RuledSurfaceFeature/RuledSurfaceFeature.md) Object

## Description

Part RuledSurfaceFeatureProxy Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_ContainingOccurrence.md) | Get the component occurrence context through which the native object is being seen through. |
| [Definition](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Definition.md) | Read-write property that gets and sets the RuledSurfaceDefinition Object associated with this feature. |
| [ExtendedName](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_NativeObject.md) | Get the source object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../RuledSurfaceFeatureProxy/RuledSurfaceFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2016
