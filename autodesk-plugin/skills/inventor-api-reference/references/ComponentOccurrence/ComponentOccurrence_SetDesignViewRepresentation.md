# ComponentOccurrence.SetDesignViewRepresentation Method

Parent Object: [ComponentOccurrence](../ComponentOccurrence/ComponentOccurrence.md)

## Description

Method that sets a design view representation for an assembly occurrence.

## Syntax

ComponentOccurrence.**SetDesignViewRepresentation**( ***Representation*** As String, [***Reserved***] As String, [***Associative***] As Boolean )

## Parameters

|  |  |  |
| --- | --- | --- |
| Name | Type | Description |
| Representation | String | String that specifies the Design View Representation to set on the occurrence. The method returns a failure if a representation with this name is not found in the referenced assembly or in the private representation file (if specified). |
| Reserved | String |  |
| Associative | Boolean | Optional input Boolean that indicates whether to associatively apply the design view. If set to True, any changes to the design view in the referenced assembly will show in this occurrence. If not specified, a value of False is used. This method fails if the input representation is a private design view representation and a value of True is specified for this argument (i.e. the associative option is invalid for private design views).   This is an optional argument whose default value is False. |

## Version

Introduced in version 11
