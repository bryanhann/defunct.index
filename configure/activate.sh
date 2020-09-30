export PYTHONPATH=
export PYTHONPATH=$PYTHONPATH:${PWD}/project/lib
export PYTHONPATH=$PYTHONPATH:${PWD}/project/bin
export PRJ_ROOT=$PWD
export PRJ_CODE=$PWD/project
export PRJ_dict=$PWD/submodules/dict.repo/dict.txt
export PRJ_eng=$PWD/submodules/units.repo/C1_20200912_1/eng.txt
export PRJ_chi=$PWD/submodules/units.repo/C1_20200912_1/chi.txt
git submodule update --init
#export GIT_ROOT_INDEX=https://github.com/bryanhann/index
#git clone $GIT_ROOT_INDEX GIT_ROOT_INDEX

