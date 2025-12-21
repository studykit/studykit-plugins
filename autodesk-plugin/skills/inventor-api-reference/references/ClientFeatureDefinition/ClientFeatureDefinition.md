# ClientFeatureDefinition Object

## Description

The ClientFeatureDefinition object is used to define and query all the inputs of a ClientFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddDependency](../ClientFeatureDefinition/ClientFeatureDefinition_AddDependency.md) | Method that adds an upstream Inventor object as a dependency of the client feature. |
| [RemoveDependency](../ClientFeatureDefinition/ClientFeatureDefinition_RemoveDependency.md) | Method that removes a dependency of the client feature. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [Application](../ClientFeatureDefinition/ClientFeatureDefinition_Application.md) | Returns the top-level parent application object. When used the context of Inventor, an Application object is returned. When used in the context of Apprentice, an ApprenticeServer object is returned. |
| [ClientFeatureElements](../ClientFeatureDefinition/ClientFeatureDefinition_ClientFeatureElements.md) | Property that returns the ClientFeatureElements collection object that defines the Inventor objects composited by this feature. |
| [ClientGraphicsCollection](../ClientFeatureDefinition/ClientFeatureDefinition_ClientGraphicsCollection.md) | Property that returns the ClientGraphicsCollection object. These graphics are persisted with the document. |
| [FeatureInputs](../ClientFeatureDefinition/ClientFeatureDefinition_FeatureInputs.md) | Read-write property that gets and sets the objects that are inputs to the client feature. |
| [FeatureType](../ClientFeatureDefinition/ClientFeatureDefinition_FeatureType.md) | Property that defines the naming of the client feature in the browser. This property returns a non-localized string supplied during the creation. |
| [GraphicsDataSetsCollection](../ClientFeatureDefinition/ClientFeatureDefinition_GraphicsDataSetsCollection.md) | Read-only property that returns the GraphicsDataSetsCollection object. |
| [HighlightClientGraphicsWithFeature](../ClientFeatureDefinition/ClientFeatureDefinition_HighlightClientGraphicsWithFeature.md) | Read-write property that gets and sets whether client graphics owned by this feature should be pre-highlighted, highlighted or selected with the client feature. |
| [Parent](../ClientFeatureDefinition/ClientFeatureDefinition_Parent.md) | Property that returns the parent ClientFeature object. The property returns Nothing in the forward create scenario (i.e. when the object is created using ClientFeatures.CreateDefinition method). |
| [Type](../ClientFeatureDefinition/ClientFeatureDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ClientFeature.Definition](../ClientFeature/ClientFeature_Definition.md), [ClientFeatureElement.Parent](../ClientFeatureElement/ClientFeatureElement_Parent.md), [ClientFeatureElementProxy.Parent](../ClientFeatureElementProxy/ClientFeatureElementProxy_Parent.md), [ClientFeatureProxy.Definition](../ClientFeatureProxy/ClientFeatureProxy_Definition.md), [ClientFeatures.CreateDefinition](../ClientFeatures/ClientFeatures_CreateDefinition.md)

## Version

Introduced in version 2008

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |