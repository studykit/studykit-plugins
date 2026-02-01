# SweepFeatureProxy Object

Derived from: [SweepFeature](../SweepFeature/SweepFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddParticipant](../SweepFeatureProxy/SweepFeatureProxy_AddParticipant.md) | Add the specified occurrence from the list of participants for this feature. This method only applies to assembly features. |
| [Delete](../SweepFeatureProxy/SweepFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../SweepFeatureProxy/SweepFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../SweepFeatureProxy/SweepFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../SweepFeatureProxy/SweepFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../SweepFeatureProxy/SweepFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../SweepFeatureProxy/SweepFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../SweepFeatureProxy/SweepFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../SweepFeatureProxy/SweepFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../SweepFeatureProxy/SweepFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../SweepFeatureProxy/SweepFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../SweepFeatureProxy/SweepFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../SweepFeatureProxy/SweepFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [ConsumeInputs](../SweepFeatureProxy/SweepFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../SweepFeatureProxy/SweepFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../SweepFeatureProxy/SweepFeatureProxy_Definition.md) | Read-write property that gets and sets the SweepDefinition object associated with this sweep feature. |
| [EndFaces](../SweepFeatureProxy/SweepFeatureProxy_EndFaces.md) | Property that returns the set of that cap one end of the sweep that are coincident with the sketch plane. The end faces are those not coincident to the sketch plane of the feature's profile. In the case of a symmetric revolution these faces are the ones on the negative normal side of the sketch plane. In the cases where there aren't any end faces this property will return Nothing. |
| [ExtendedName](../SweepFeatureProxy/SweepFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../SweepFeatureProxy/SweepFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../SweepFeatureProxy/SweepFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../SweepFeatureProxy/SweepFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [IsOwnedByFeature](../SweepFeatureProxy/SweepFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [IsSolidSweep](../SweepFeatureProxy/SweepFeatureProxy_IsSolidSweep.md) | Read-only property that returns whether the feature is a solid sweep feature. |
| [Name](../SweepFeatureProxy/SweepFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../SweepFeatureProxy/SweepFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../SweepFeatureProxy/SweepFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../SweepFeatureProxy/SweepFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../SweepFeatureProxy/SweepFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../SweepFeatureProxy/SweepFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../SweepFeatureProxy/SweepFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../SweepFeatureProxy/SweepFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [SideFaces](../SweepFeatureProxy/SweepFeatureProxy_SideFaces.md) | Property that returns a object that provides access to all of the faces created around the perimeter of the feature. |
| [SolidSweepDefinition](../SweepFeatureProxy/SweepFeatureProxy_SolidSweepDefinition.md) | Read-write property that gets and sets the SolidSweepDefinition object associated with this sweep feature. |
| [Suppressed](../SweepFeatureProxy/SweepFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../SweepFeatureProxy/SweepFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../SweepFeatureProxy/SweepFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 9
