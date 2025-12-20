# ClientFeature Object

Derived from: [PartFeature](../PartFeature/PartFeature.md) Object

## Description

The ClientFeature object represents a client feature in a part or an assembly document. A client feature is stored in Inventor's data model, and it's behaviors are provided jointly by Inventor and the client. It is an object that can composite other objects, and it can persist client graphics with a document.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Delete](../ClientFeature/ClientFeature_Delete.md) | Method that deletes the feature. The arguments allow control over which dependent objects are also deleted. |
| [GetReferenceKey](../ClientFeature/ClientFeature_GetReferenceKey.md) | Method that generates and returns the reference key for this entity. |
| [GetSuppressionCondition](../ClientFeature/ClientFeature_GetSuppressionCondition.md) | Method that gets the suppression condition for the feature. The method returns False if no condition has been applied. |
| [RemoveParticipant](../ClientFeature/ClientFeature_RemoveParticipant.md) | Method that removes the specified participant from the assembly feature. This method fails for features in a part. |
| [SetAffectedBodies](../ClientFeature/ClientFeature_SetAffectedBodies.md) | Method that sets a collection of SurfaceBody objects affected by this feature. |
| [SetEndOfPart](../ClientFeature/ClientFeature_SetEndOfPart.md) | Method that repositions the end-of-part marker relative to the object this method is called from. |
| [SetSuppressionCondition](../ClientFeature/ClientFeature_SetSuppressionCondition.md) | Method that sets the suppression condition for the feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Adaptive](../ClientFeature/ClientFeature_Adaptive.md) | Gets and sets whether this feature is adaptive or not. |
| [Appearance](../ClientFeature/ClientFeature_Appearance.md) | Gets and sets the current appearance of the feature. |
| [AppearanceSourceType](../ClientFeature/ClientFeature_AppearanceSourceType.md) | Gets and sets the source of the appearance for the feature. |
| [Application](../ClientFeature/ClientFeature_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [AttributeSets](../ClientFeature/ClientFeature_AttributeSets.md) | Property that returns the AttributeSets collection object associated with this object. |
| [BrowserNode](../ClientFeature/ClientFeature_BrowserNode.md) | Property that returns the BrowserNode object in the model browser associated with this client feature. |
| [ClientGraphicsVisible](../ClientFeature/ClientFeature_ClientGraphicsVisible.md) | Property that gets and sets whether all the client graphics in this client featureare visible or not.When getting this property valid values are kAllGraphicsVisible,kNoGraphicsVisible, and kSomeGraphicsVisible. When setting this propertykAllGraphicsVisible and. |
| [ClientId](../ClientFeature/ClientFeature_ClientId.md) | Property that returns the string that uniquely identifies the client. This is the CLSID of the AddIn in a string form, e.g. "{C9A6C580-3817-11D0-BE4E-080036E87B02}". |
| [ConsumeInputs](../ClientFeature/ClientFeature_ConsumeInputs.md) | Gets and sets whether the inputs to this feature should be nested under this feature in the browser. |
| [Definition](../ClientFeature/ClientFeature_Definition.md) | Property that returns the ClientFeatureDefinition object that specifies the various inputs used to create the feature. |
| [ExtendedName](../ClientFeature/ClientFeature_ExtendedName.md) | Read-only property that returns the full feature name including any extended information. |
| [Faces](../ClientFeature/ClientFeature_Faces.md) | Property that returns a collection that provides access to all of the faces of the feature. The Faces collection object will return the faces that still currently exist in the part. For example, if a face has been consumed by additional modeling operations it will not be returned. |
| [FeatureDimensions](../ClientFeature/ClientFeature_FeatureDimensions.md) | Property that returns the FeatureDimensions collection object. |
| [HealthStatus](../ClientFeature/ClientFeature_HealthStatus.md) | Property that returns an enum indicating the current state of the object. |
| [HiddenParameters](../ClientFeature/ClientFeature_HiddenParameters.md) | Read-write property that gets and sets the collection of Parameters that are to be hidden from the user. |
| [IsOwnedByFeature](../ClientFeature/ClientFeature_IsOwnedByFeature.md) | Property that returns whether this object is owned by a feature. If True, the OwnedBy property returns the owning feature. |
| [Name](../ClientFeature/ClientFeature_Name.md) | Gets/Sets the name of this Part Feature within the scope of this Document. |
| [OwnedBy](../ClientFeature/ClientFeature_OwnedBy.md) | Property that returns the owning PartFeature object. This property returns Nothing if the IsOwnedByFeature property returns False. |
| [Parameters](../ClientFeature/ClientFeature_Parameters.md) | Property that returns all the parameters associated with the feature. |
| [Parent](../ClientFeature/ClientFeature_Parent.md) | Property that returns the parent of the feature. |
| [Participants](../ClientFeature/ClientFeature_Participants.md) | Property that returns the list of participants for an assembly feature. This list is empty for features in a part. |
| [RangeBox](../ClientFeature/ClientFeature_RangeBox.md) | Property that returns a Box object which contains the opposing points of a rectangular box that is guaranteed to enclose this object. |
| [Shared](../ClientFeature/ClientFeature_Shared.md) | Gets and sets whether the part feature is shared or not, applies only to surface features. |
| [Suppressed](../ClientFeature/ClientFeature_Suppressed.md) | Gets and sets whether this feature is suppressed or not. |
| [SurfaceBodies](../ClientFeature/ClientFeature_SurfaceBodies.md) | Property that returns the bodies that this feature has created or modified. |
| [Type](../ClientFeature/ClientFeature_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ClientFeatureDefinition.Parent](../ClientFeatureDefinition/ClientFeatureDefinition_Parent.md), [ClientFeatureProxy.NativeObject](../ClientFeatureProxy/ClientFeatureProxy_NativeObject.md), [ClientFeatures.Add](../ClientFeatures/ClientFeatures_Add.md), [ClientFeatures.Item](../ClientFeatures/ClientFeatures_Item.md)

## Derived Classes

[ClientFeatureProxy](../ClientFeatureProxy/ClientFeatureProxy.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |