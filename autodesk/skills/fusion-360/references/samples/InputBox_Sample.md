# Use inputBox to get value and evaluateExpression to validate it

## Description

Uses the UserInterface.inputBox function to get a string from the user and then validates that the strinng entered is a valid expression by using the UnitsManager.evaluateExpression function.

## Code Samples

* [C++](#C++)
* [Python](#Python)

|  |
| --- |
| Copy Code |

```
#include <Core/Application/Application.h>
#include <Core/UserInterface/UserInterface.h>
#include <Core/Utils.h>
#include <Fusion/Fusion/Design.h>
#include <Fusion/Fusion/FusionUnitsManager.h>
#include <sstream>

using namespace adsk::core;
using namespace adsk::fusion;

Ptr<UserInterface> ui;

extern "C" XI_EXPORT bool run(const char* context)
{
    Ptr<Application> app = Application::get();
    if (!app)
        return false;

    ui = app->userInterface();
    if (!ui)
        return false;

    Ptr<Design> design = app->activeProduct();
    if (!design)
    {
        ui->messageBox("No active Fusion design", "No Design");
        return false;
    }

    // Prompt the user for a string and validate it's valid.
    bool isValid = false;
    std::string input = "1 in"; // The initial default value.
    double realValue = 0.0;
    while (!isValid)
    {
        // Get a string from the user.
        bool cancelled = false;
        input = ui->inputBox("Enter a distance", cancelled, "Distance", input);

        // Exit the program if the dialog was cancelled.
        if (cancelled)
        {
            adsk::terminate();
            return false;
        }

        // Check that a valid length description was entered.
        Ptr<UnitsManager> unitsMgr = design->unitsManager();
        if (!unitsMgr)
            return false;

        realValue = unitsMgr->evaluateExpression(input, unitsMgr->defaultLengthUnits());
        if (app->getLastError())
        {
            // Invalid expression so display an error and set the flag to allow them
            // to enter a value again.
            ui->messageBox(
                input + " is not a valid length expression.", "Invalid entry", OKButtonType, CriticalIconType);
            isValid = false;
        }
        else
            isValid = true;
    }

    // Use the value for something.
    std::stringstream ss;
    ss << "input: " << input << ", result: " << realValue;
    ui->messageBox(ss.str());

    return true;
}
```

|  |
| --- |
| Copy Code |

```
#Author-
#Description-
import adsk.core, adsk.fusion, traceback

def run(context):
    ui = None
    try:
        app = adsk.core.Application.get()
        ui = app.userInterface
        design = app.activeProduct
        if not design:
            ui.messageBox('No active Fusion design', 'No Design')
            return

        # Prompt the user for a string and validate it's valid.
        isValid = False
        input = '1 in'  # The initial default value.
        while not isValid:
            # Get a string from the user.
            retVals = ui.inputBox('Enter a distance', 'Distance', input)
            if retVals[0]:
                (input, isCancelled) = retVals

            # Exit the program if the dialog was cancelled.
            if isCancelled:
                return

            # Check that a valid length description was entered.
            unitsMgr = design.unitsManager
            try:
                realValue = unitsMgr.evaluateExpression(input, unitsMgr.defaultLengthUnits)
                isValid = True
            except:
                # Invalid expression so display an error and set the flag to allow them
                # to enter a value again.
                ui.messageBox('"' + input + '" is not a valid length expression.', 'Invalid entry',
                              adsk.core.MessageBoxButtonTypes.OKButtonType,
                              adsk.core.MessageBoxIconTypes.CriticalIconType)
                isValid = False

        # Use the value for something.
        ui.messageBox('input: ' + input + ', result: ' + str(realValue))

    except:
        if ui:
            ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
```

---

|  |  |
| --- | --- |
| © Copyright 2025 Autodesk, Inc. | Comment on this page. |