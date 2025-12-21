# MoveFeatureProxy Object

Derived from: [MoveFeature](../MoveFeature/MoveFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../MoveFeatureProxy/MoveFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../MoveFeatureProxy/MoveFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../MoveFeatureProxy/MoveFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../MoveFeatureProxy/MoveFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../MoveFeatureProxy/MoveFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../MoveFeatureProxy/MoveFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../MoveFeatureProxy/MoveFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../MoveFeatureProxy/MoveFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../MoveFeatureProxy/MoveFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../MoveFeatureProxy/MoveFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../MoveFeatureProxy/MoveFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../MoveFeatureProxy/MoveFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../MoveFeatureProxy/MoveFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../MoveFeatureProxy/MoveFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../MoveFeatureProxy/MoveFeatureProxy_Definition.md) | Gets and sets the definition for the move feature. |
| [ExtendedName](../MoveFeatureProxy/MoveFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../MoveFeatureProxy/MoveFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../MoveFeatureProxy/MoveFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../MoveFeatureProxy/MoveFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../MoveFeatureProxy/MoveFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../MoveFeatureProxy/MoveFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../MoveFeatureProxy/MoveFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../MoveFeatureProxy/MoveFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../MoveFeatureProxy/MoveFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../MoveFeatureProxy/MoveFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../MoveFeatureProxy/MoveFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../MoveFeatureProxy/MoveFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../MoveFeatureProxy/MoveFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../MoveFeatureProxy/MoveFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../MoveFeatureProxy/MoveFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Transformation](../MoveFeatureProxy/MoveFeatureProxy_Transformation.md) | A transformation matrix that moves an extrude, revolve, or sweep feature to a new location. |
| [Type](../MoveFeatureProxy/MoveFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2010
