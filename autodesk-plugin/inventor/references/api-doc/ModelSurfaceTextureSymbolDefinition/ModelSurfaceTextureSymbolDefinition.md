# ModelSurfaceTextureSymbolDefinition Object

## Description

ModelSurfaceTextureSymbolDefinition Object.

## Methods

|  |  |
| --- | --- |
| Name | Description |
| [AddLeader](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AddLeader.md) | Method that adds a leader branch with the input points. This is the equivalent of the 'Add Leader' command in the user interface. This method will succeed only if the HasRootNode property returns False (i.e. there are no existing leader segments). If there are existing leader segments, you should use the ModelLeaderNode.AddLeader method instead. |
| [Copy](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Copy.md) | Method that creates a copy of this ModelSurfaceTextureSymbolDefinition object. The new ModelSurfaceTextureSymbolDefinition object is independent of any surface texture symbols. It can edited and used as input to edit an existing surface texture symbol or to create a new surface texture symbol. |

## Properties

|  |  |
| --- | --- |
| Name | Description |
| [AdditionalProductionMethod](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AdditionalProductionMethod.md) | Read-write property that gets and sets an additional tail for the production method if the drafting standard is based on ISO or DIN. Setting this property will return an error if the ProductionMethod property is not specified. Denoted by B' in the surface tex. |
| [AdditionalRoughness](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AdditionalRoughness.md) | Read-write property that gets and sets the roughness value other than Ra or the parameter value other than Ra. For ANSI, this property can also be used to specify the waviness height. Denoted by F in the surface texture symbol dialog. |
| [AdditionalSamplingLength](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AdditionalSamplingLength.md) | Read-write property that gets and sets the following: (1)the roughness cutoff or sampling length for additional roughness value for ANSI (2)the sampling length for additional roughness value for ISO or DIN (3)the reference length and evaluation length for JIS. |
| [AllAroundSymbol](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AllAroundSymbol.md) | Read-write property that gets and sets whether to add the all-around indicator to the symbol. |
| [AllLeafNodes](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AllLeafNodes.md) | Read-only that returns a flat collection of all the leaf nodes in the leader tree. This property will return Nothing if the HasRootNode property returns False. |
| [AllNodes](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AllNodes.md) | Read-only that returns a flat collection of all the nodes in the leader tree. This property will return Nothing if the HasRootNode property returns False. |
| [AnnotationPlane](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AnnotationPlane.md) | Read-write property that gets and sets the annotation plane for the symbol. |
| [AnnotationPlaneDefinition](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_AnnotationPlaneDefinition.md) | Read-write property that gets and sets the annotation plane definition for the symbol. |
| [Application](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Application.md) | Gets the root Application object. Where the property is weakly-typed, it can be set to (QueryInterfaced for) 'Application' when running with Inventor whereas, 'ApprenticeServer' when running with the Apprentice Server. |
| [Faces](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Faces.md) | Gets or sets the faces the surface texture symbol is associative with. |
| [HasRootNode](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_HasRootNode.md) | Read-only property that returns if a root node exists for this leader. If False, there are no leader segments associated with this leader and the RootNode property will return Nothing. |
| [Intent](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Intent.md) | Read-write property that gets and sets the geometric entity the note is attached to. |
| [IsForceTailShown](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_IsForceTailShown.md) | Read-write property that gets and sets whether a tail is added to the symbol. |
| [IsMajority](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_IsMajority.md) | Read-write property that gets and sets whether this symbol specifies the standard surface characteristics for the component. |
| [LayDirection](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_LayDirection.md) | Read-write property that gets and sets the direction of lay. Setting this property will return an error if the SurfaceTextureType is specified to be kMaterialRemovalProhibitedSurfaceType. Denoted by D in the surface texture symbol dialog. |
| [Leader](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Leader.md) | Read-only property that returns the leader associated with the leader note. |
| [MachiningAllowance](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_MachiningAllowance.md) | Read-write property that gets and sets the machining allowance. Setting this property will return an error if the SurfaceTextureType is not kMaterialRemovalRequiredSurfaceType. Denoted by E in the surface texture symbol dialog. |
| [ManufacturingProcess](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_ManufacturingProcess.md) | Gets and sets the manufacturing process. |
| [MaximumRoughness](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_MaximumRoughness.md) | Read-write property that gets and sets the roughness value, roughness value Ra maximum, maximum roughness value, or grade number. Denoted by A' in the surface texture symbol dialog. |
| [MinimumRoughness](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_MinimumRoughness.md) | Read-write property that gets and sets the roughness value, roughness value Ra minimum, minimum roughness value, or grade number. Setting this property will return an error if the MaximumRoughness property is not specified. Denoted by A in the surface texture. |
| [NumberOfFeatureElements](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_NumberOfFeatureElements.md) | Gets and sets the number of feature elements. |
| [Parent](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Parent.md) | Gets the parent object from whom this object can logically be reached. |
| [Position](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Position.md) | Gets and sets the position of the symbol on the model. |
| [ProductionMethod](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_ProductionMethod.md) | Read-write property that gets and sets the production method, treatment, or coating. If the active drafting standard is based on ANSI, this property can be used to specify a note callout. Denoted by B in the surface texture symbol dialog. |
| [ProfileDirection](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_ProfileDirection.md) | Gets and sets the profile direction relative to primary surface lay direction. |
| [RootNode](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_RootNode.md) | Read-only property that returns the root node of this leader. This property will return Nothing if the HasRootNode property returns False. |
| [SamplingLength](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_SamplingLength.md) | Read-write property that gets and sets the following: (1)the roughness cutoff or sampling length for roughness average for ANSI (2)the waviness height or sampling length for ISO or DIN (3)the cutoff value and evaluation length for JIS. |
| [StandardReference](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_StandardReference.md) | Returns the standard reference type. |
| [SurfaceProfileLowerTolerance](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_SurfaceProfileLowerTolerance.md) | Gets and sets the surface profile lower tolerance. |
| [SurfaceProfileUpperTolerance](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_SurfaceProfileUpperTolerance.md) | Gets and sets the surface profile upper tolerance. |
| [SurfaceTextureType](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_SurfaceTextureType.md) | Read-write property that gets and sets the surface type for the symbol. Possible values kBasicSurfaceType, kMaterialRemovalRequiredSurfaceType and kMaterialRemovalProhibitedSurfaceType. |
| [SurfaceWaviness](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_SurfaceWaviness.md) | Read-write property that gets and sets the surface waviness for JIS, or general comments for BSI. This property is ignored for ANSI, ISO, or DIN standards. Denoted by F' or G in the surface texture symbol dialog. |
| [Type](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Type.md) | Returns an ObjectTypeEnum indicating this object's type. |

## Accessed From

[ModelGeneralNotes.CreateEmbeddedSurfaceTextureSymbolDefinition](../ModelGeneralNotes/ModelGeneralNotes_CreateEmbeddedSurfaceTextureSymbolDefinition.md), [ModelSurfaceTextureSymbol.Definition](../ModelSurfaceTextureSymbol/ModelSurfaceTextureSymbol_Definition.md), [ModelSurfaceTextureSymbolDefinition.Copy](../ModelSurfaceTextureSymbolDefinition/ModelSurfaceTextureSymbolDefinition_Copy.md), [ModelSurfaceTextureSymbolProxy.Definition](../ModelSurfaceTextureSymbolProxy/ModelSurfaceTextureSymbolProxy_Definition.md), [ModelSurfaceTextureSymbols.CreateDefinition](../ModelSurfaceTextureSymbols/ModelSurfaceTextureSymbols_CreateDefinition.md)

## Version

Introduced in version 2018

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |