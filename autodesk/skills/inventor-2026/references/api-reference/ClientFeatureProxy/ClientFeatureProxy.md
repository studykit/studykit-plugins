# ClientFeatureProxy Object

Derived from: [ClientFeature](../ClientFeature/ClientFeature.md) Object

## Description

This is an assembly-context proxy object derived from its native definition-context object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ClientFeatureProxy/ClientFeatureProxy_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ClientFeatureProxy/ClientFeatureProxy_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ClientFeatureProxy/ClientFeatureProxy_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ClientFeatureProxy/ClientFeatureProxy_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ClientFeatureProxy/ClientFeatureProxy_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ClientFeatureProxy/ClientFeatureProxy_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ClientFeatureProxy/ClientFeatureProxy_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ClientFeatureProxy/ClientFeatureProxy_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ClientFeatureProxy/ClientFeatureProxy_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ClientFeatureProxy/ClientFeatureProxy_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ClientFeatureProxy/ClientFeatureProxy_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ClientFeatureProxy/ClientFeatureProxy_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BrowserNode](../ClientFeatureProxy/ClientFeatureProxy_BrowserNode.md) | Property that returns the BrowserNode object in the model browser associated with this client feature. |
| [ClientGraphicsVisible](../ClientFeatureProxy/ClientFeatureProxy_ClientGraphicsVisible.md) | Property that gets and sets whether all the client graphics in this client featureare visible or not.When getting this property valid values are kAllGraphicsVisible,kNoGraphicsVisible, and kSomeGraphicsVisible. When setting this propertykAllGraphicsVisible and. |
| [ClientId](../ClientFeatureProxy/ClientFeatureProxy_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [ConsumeInputs](../ClientFeatureProxy/ClientFeatureProxy_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [ContainingOccurrence](../ClientFeatureProxy/ClientFeatureProxy_ContainingOccurrence.md) | Property that returns the ComponentOccurrence that the native object is being referenced through. The returned occurrence is the containing occurrence. |
| [Definition](../ClientFeatureProxy/ClientFeatureProxy_Definition.md) | Property that returns the ClientFeatureDefinition object that specifies the various inputs used to create the feature. |
| [ExtendedName](../ClientFeatureProxy/ClientFeatureProxy_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ClientFeatureProxy/ClientFeatureProxy_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ClientFeatureProxy/ClientFeatureProxy_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ClientFeatureProxy/ClientFeatureProxy_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [HiddenParameters](../ClientFeatureProxy/ClientFeatureProxy_HiddenParameters.md) | Read-write property that gets and sets the collection of Parameters that are to be hidden from the user. |
| [IsOwnedByFeature](../ClientFeatureProxy/ClientFeatureProxy_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ClientFeatureProxy/ClientFeatureProxy_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [NativeObject](../ClientFeatureProxy/ClientFeatureProxy_NativeObject.md) | Gets the object in the context of the definition instead of the containing assembly. |
| [OwnedBy](../ClientFeatureProxy/ClientFeatureProxy_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ClientFeatureProxy/ClientFeatureProxy_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ClientFeatureProxy/ClientFeatureProxy_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ClientFeatureProxy/ClientFeatureProxy_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ClientFeatureProxy/ClientFeatureProxy_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ClientFeatureProxy/ClientFeatureProxy_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../ClientFeatureProxy/ClientFeatureProxy_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ClientFeatureProxy/ClientFeatureProxy_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ClientFeatureProxy/ClientFeatureProxy_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Version

Introduced in version 2008
