# FaceDraftDefinition Object

## Description

The FaceDraftDefinition object represents the definition for a FaceDraftFeature.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [Copy](../FaceDraftDefinition/FaceDraftDefinition_Copy.md) | Method that creates a copy of this FaceDraftDefinition object. The new FaceDraftDefinition object is independent of any feature. It can be edited and used as input to edit an existing feature or to create a new face draft feature. |
| [SetFixedEdge](../FaceDraftDefinition/FaceDraftDefinition_SetFixedEdge.md) | Method that set the face draft definition to be kFixedEdgeFaceDraftDefinitionType with input values. |
| [SetFixedPlane](../FaceDraftDefinition/FaceDraftDefinition_SetFixedPlane.md) | Method that set the face draft definition to be kFixedPlaneFaceDraftDefinitionType with input values. |
| [SetPartingTool](../FaceDraftDefinition/FaceDraftDefinition_SetPartingTool.md) | Method that set the face draft definition to be kPartingToolFaceDraftDefinitionType with input values. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AbsoluteDraftAngle](../FaceDraftDefinition/FaceDraftDefinition_AbsoluteDraftAngle.md) | Read-write property that gets and sets whether the draft angle of the face draft is absolute against the pull direction. |
| [Application](../FaceDraftDefinition/FaceDraftDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [AutomaticBlending](../FaceDraftDefinition/FaceDraftDefinition_AutomaticBlending.md) | Read-write property that gets and sets whether include the blended features in the face draft feature. |
| [CutMaterial](../FaceDraftDefinition/FaceDraftDefinition_CutMaterial.md) | Read-write property that gets and sets whether to cut material or not when create a draft face feature using parting tool. This is applicable only when the DefinitionType is kPartingToolFaceDraftDefinitionType. |
| [DefinitionType](../FaceDraftDefinition/FaceDraftDefinition_DefinitionType.md) | Read-only property that returns the FaceDraftDefinitionTypeEnum indicating which face draft type the definition is. |
| [DraftAngle](../FaceDraftDefinition/FaceDraftDefinition_DraftAngle.md) | Read-write property that gets and sets the draft angle of the face draft. For parting line face draft, this DraftAngle will be the minimum draft angle value for the two sides face draft. |
| [DraftAngleConstraintType](../FaceDraftDefinition/FaceDraftDefinition_DraftAngleConstraintType.md) | Read-write property that gets and sets the draft angle constraint type for the face draft. |
| [DraftAngleTwo](../FaceDraftDefinition/FaceDraftDefinition_DraftAngleTwo.md) | Read-write property that gets and sets the draft angle two of the face draft. This property is applicable only when the DraftAngleConstraintType is set to kAsymmetricDraftAngles. |
| [FixedEdges](../FaceDraftDefinition/FaceDraftDefinition_FixedEdges.md) | Read-write property that gets and sets the fixed edges on the input faces. This property is applicable when the DefinitionType is kFixedEdgeFaceDraftDefinitionType or kPartingToolFaceDraftDefinitionType and the CutMaterial is False. |
| [InputFaces](../FaceDraftDefinition/FaceDraftDefinition_InputFaces.md) | Read-write property that specifies the faces used to create the feature. |
| [Parent](../FaceDraftDefinition/FaceDraftDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [PullDirection](../FaceDraftDefinition/FaceDraftDefinition_PullDirection.md) | Read-only property that specifies the object used to determine the pull direction. For a fixed edge face draft this could be a planar Face, an Edge, a WorkPlane or a WorkAxis. For a fixed plane face draft this could either be a planar Face or a WorkPlane. |
| [PullDirectionReversed](../FaceDraftDefinition/FaceDraftDefinition_PullDirectionReversed.md) | Read-write property that gets and sets whether reverse the pull direction. |
| [Type](../FaceDraftDefinition/FaceDraftDefinition_Type.md) | Gets the constant that indicates the type of this object. |

## Accessed From

[FaceDraftDefinition.Copy](../FaceDraftDefinition/FaceDraftDefinition_Copy.md), [FaceDraftFeature.Definition](../FaceDraftFeature/FaceDraftFeature_Definition.md), [FaceDraftFeatureProxy.Definition](../FaceDraftFeatureProxy/FaceDraftFeatureProxy_Definition.md), [FaceDraftFeatures.CreateFaceDraftDefinition](../FaceDraftFeatures/FaceDraftFeatures_CreateFaceDraftDefinition.md)

## Version

Introduced in version 2016

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |