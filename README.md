# Running D-Tale in Binder

This repo can be used an example for how to use [D-Tale](https://github.com/man-group/dtale) within a Binder environment.

The main things to note are:
* include `jupyter-server-proxy` in your [environment.yaml](https://github.com/aschonfeld/dtale-binder/blob/master/environment.yml)
* activate `jupyter-server-proxy` using a [postBuild file](https://github.com/aschonfeld/dtale-binder/blob/master/postBuild)

I've provided an example of a notebook that uses D-Tale [here](https://github.com/aschonfeld/dtale-binder/blob/master/Running_dtale.ipynb)

If D-Tale does not display in the output underneath your notebook cell then be sure to check the value of your instance's `_main_url`. For example:
```python
import dtale
import dtale.app as dtale_app
import pandas as pd

dtale_app.JUPYTER_SERVER_PROXY = True

d = dtale.show(pd.DataFrame([1,2,3,4,5]))
d._main_url
```

The output of that value should get appended to the host of your Binder notebook to view D-Tale.  Currently the Binder host is `https://hub.gke2.mybinder.org` so ideally you would just need to concatenate that hostname to the value of `_main_url` and paste taht value in a new browser tab to view D-Tale.  Please submit bugs to the [D-Tale repo](https://github.com/man-group/dtale) if that's not the case.
